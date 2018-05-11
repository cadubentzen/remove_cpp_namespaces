namespace foo {
void goo()
{
}
}

int main(int argc, char* argv[])
{
    foo::goo();
    ::foo::goo();

    return 0;
}
