#
# PySNMP MIB module SNMPv2-TC-EXT-01 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMPv2-TC-EXT-01
# Produced by pysmi-0.3.4 at Wed May  1 15:08:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, IpAddress, Counter32, MibIdentifier, ModuleIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, TimeTicks, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "ModuleIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "TimeTicks", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class InternationalString(TextualConvention, OctetString):
    description = 'An octet string containing human-readable information. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 transformation format described in [RFC2279]. Since additional code points are added by amendments to the 10646 standard from time to time, implementations must be prepared to encounter any code point from 0x00000000 to 0x7fffffff. Byte sequences that do not correspond to the valid UTF-8 encoding of a code point or are outside this range are prohibited. The use of control codes should be avoided. When it is necessary to represent a newline, the control code sequence CR LF should be used. For code points not directly supported by user interface hardware or software, an alternative means of entry and display, such as hexadecimal, may be provided. For information encoded in 7-bit US-ASCII, the UTF-8 encoding is identical to the US-ASCII encoding. UTF-8 may require multiple bytes to represent a single character / code point; thus the length of this object in octets may be different from the number of characters encoded. Similarly, size constraints refer to the number of encoded octets, not the number of characters represented by an encoding. Note that when this TC is used for an object that is used or envisioned to be used as an index, then a SIZE restriction MUST be specified so that the number of sub-identifiers for any object instance does not exceed the limit of 128, as defined by [RFC1905]. Note that the size of an InternationalString object is measured in octets, not characters.'
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TAddressOrZero(TextualConvention, OctetString):
    description = 'Denotes a transport service address. A zero-length octet string indicates that no transport address is known. A TAddress value is always interpreted within the context of a TDomain value. Thus, each definition of a TDomain value must be accompanied by a definition of a textual convention for use with that TDomain. Some possible textual conventions, such as SnmpUDPAddress for snmpUDPDomain, are defined in the SNMPv2-TM MIB module. Other possible textual conventions are defined in other MIB modules. Note, the definition of this textual convention is identical to the TAddress definition in the SNMPv2-TM MIB module with the only difference that this textual convention allows a zero-length TAddress value.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TAddressMask(TextualConvention, OctetString):
    description = 'Denotes a transport service address mask. A mask value is used to select which bits of a transport address must match bits of the corresponding instance of a TAddress object. The value of an instance of this textual convention must always be an OCTET STRING whose length is either zero or the same as that of the corresponding instance of a TAddress object. The matching algorithm is as follows: Each bit of each octet in the TAddressMask value corresponds to the same bit of the same octet in the TAddress value. For bits that are set in the TAddressMask value (i.e. bits equal to 1), the corresponding bits in the TAddress value must match the bits in a given transport address. If all such bits match, the transport address is matched. Otherwise, the match fails.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class TAddressMaskOrZero(TextualConvention, OctetString):
    description = 'Denotes a transport service address mask. A zero-length octet string indicates that the match always succeeds. A mask value is used to select which bits of a transport address must match bits of the corresponding instance of a TAddress object. The value of an instance of this textual convention must always be an OCTET STRING whose length is either zero or the same as that of the corresponding instance of a TAddress object. The matching algorithm is as follows: If the value of the TAddressMask is a zero-length OCTET STRING, the mask value is ignored and the match succeeds. Otherwise, each bit of each octet in the TAddressMask value corresponds to the same bit of the same octet in the TAddress value. For bits that are set in the TAddressMask value (i.e. bits equal to 1), the corresponding bits in the TAddress value must match the bits in a given transport address. If all such bits match, the transport address is matched. Otherwise, the match fails.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("SNMPv2-TC-EXT-01", TAddressMask=TAddressMask, TAddressMaskOrZero=TAddressMaskOrZero, InternationalString=InternationalString, TAddressOrZero=TAddressOrZero)
