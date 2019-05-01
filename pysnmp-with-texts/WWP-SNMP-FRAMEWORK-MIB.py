#
# PySNMP MIB module WWP-SNMP-FRAMEWORK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-SNMP-FRAMEWORK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Counter64, iso, ModuleIdentity, Counter32, Gauge32, MibIdentifier, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Counter64", "iso", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpSnmpFrameworkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 10000))
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setLastUpdated('200510130000Z')
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setOrganization('WWP')
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setContactInfo('http://grouper.ieee.org/groups/802/1/index.html')
if mibBuilder.loadTexts: wwpSnmpFrameworkMIB.setDescription('WWP Proprietory MIB.')
class SnmpAdminString(TextualConvention, OctetString):
    description = 'An octet string containing administrative information, preferably in human-readable form. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 transformation format described in [RFC2279]. Since additional code points are added by amendments to the 10646 standard from time to time, implementations must be prepared to encounter any code point from 0x00000000 to 0x7fffffff. Byte sequences that do not correspond to the valid UTF-8 encoding of a code point or are outside this range are prohibited. The use of control codes should be avoided. When it is necessary to represent a newline, the control code sequence CR LF should be used. The use of leading or trailing white space should be avoided. For code points not directly supported by user interface hardware or software, an alternative means of entry and display, such as hexadecimal, may be provided. For information encoded in 7-bit US-ASCII, the UTF-8 encoding is identical to the US-ASCII encoding. UTF-8 may require multiple bytes to represent a single character / code point; thus the length of this object in octets may be different from the number of characters encoded. Similarly, size constraints refer to the number of encoded octets, not the number of characters represented by an encoding. Note that when this TC is used for an object that is used or envisioned to be used as an index, then a SIZE restriction MUST be specified so that the number of sub-identifiers for any object instance does not exceed the limit of 128, as defined by [RFC1905]. Note that the size of an SnmpAdminString object is measured in octets, not characters. '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("WWP-SNMP-FRAMEWORK-MIB", PYSNMP_MODULE_ID=wwpSnmpFrameworkMIB, wwpSnmpFrameworkMIB=wwpSnmpFrameworkMIB, SnmpAdminString=SnmpAdminString)
