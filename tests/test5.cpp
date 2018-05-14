namespace foo {
void goo()
{
}
} // namespace foo

int main(int argc, char* argv[])
{
    foo::goo();
    ::foo::goo();

    return 0;
}
