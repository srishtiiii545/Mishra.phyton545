{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMto1rrMdlsBa8G4mflcsmM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/srishtiiii545/Mishra.phyton545/blob/main/loop.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "1Df7p_Wequxj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OMXHQI4Bh1C-"
      },
      "outputs": [],
      "source": [
        "# print(\"hi\")\n",
        "# a=1\n",
        "# b=2\n",
        "# c=type(a)\n",
        "# print(\"type value of c\")\n",
        "# print(c)\n",
        "# m=input()\n",
        "# n=input()\n",
        "# print(int(m)+int(n))\n",
        "# c=input()\n",
        "# h=input()\n",
        "# print(int(c)-int(h))\n",
        "# k=input()\n",
        "# l=input()\n",
        "# print(int(k)*int(l))\n",
        "t=input()\n",
        "s=input()\n",
        "print(int(t)/int(s))\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input('enter the value')\n",
        "print(type(a))\n",
        "a=bool(a)\n",
        "print(type (a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l3qMqKhltKJu",
        "outputId": "f5ee3ee5-0bee-4d91-fe8f-eb0e8673bfd1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the value4\n",
            "<class 'str'>\n",
            "<class 'bool'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input()\n",
        "b=input()\n",
        "c=input()\n",
        "a=int(a)\n",
        "b=int(b)\n",
        "c=int(c)\n",
        "d=a+b+c\n",
        "if d<8:\n",
        " print('true')\n",
        "elif a-b>c:\n",
        "  print('both are even')\n",
        "else:\n",
        "  print('false')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q0r0_XLJwZYI",
        "outputId": "338faf5a-005d-4bd8-aee1-1cd25e508950"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "4\n",
            "18\n",
            "false\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input()\n",
        "a=int(a)\n",
        "if a%3==0:\n",
        " print('a is divisible by 3')\n",
        "elif a%4==0:\n",
        "  print('a is divisible by 4')\n",
        "elif a% 5==0:\n",
        "  print('a is divisible by 5')\n",
        "else :\n",
        "  print('a is not divisible by 3,4,5')\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WVxNjdv1zmhe",
        "outputId": "1487257c-1cd4-418a-eeb7-c03141a7fa83"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "17\n",
            "a is not divisible by 3,4,5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "if 5<2:\n",
        " print('5 is bigger')\n",
        "else :\n",
        "  print('condition is false')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1z-oIIOCuaqY",
        "outputId": "6048c8fd-5189-4e48-9236-1d999818f4fc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "condition is false\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=input()\n",
        "a=int(a)\n",
        "if a<=10:\n",
        "  if a==1:\n",
        "    print(\"one\")\n",
        "  elif a==2:\n",
        "    print(\"two\")\n",
        "  elif a==3:\n",
        "    print(\"three\")\n",
        "  elif a==4:\n",
        "    print(\"four\")\n",
        "  elif a==5:\n",
        "    print(\"five\")\n",
        "  elif a==6:\n",
        "    print(\"six\")\n",
        "  elif a==7:\n",
        "    print(\"seven\")\n",
        "  elif a==8:\n",
        "    print(\"eight\")\n",
        "  elif a==9:\n",
        "    print(\"nine\")\n",
        "  elif a==10:\n",
        "    print(\"ten\")\n",
        "else:\n",
        "    print(\"a is greater than 10\")\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D9m34GYT2Rup",
        "outputId": "5cfc291a-9516-4018-c355-63ccf2d25a5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "88\n",
            "a is greater than 10\n"
          ]
        }
      ]
    }
  ]
}