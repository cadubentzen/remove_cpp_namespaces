namespace foo {
namespace goo {
void hoo() {}
} // namespace goo
} // namespace foo

int main(int argc, char* argv[])
{
    foo::goo::hoo();
    ::foo::goo::hoo();

    return 0;
}
