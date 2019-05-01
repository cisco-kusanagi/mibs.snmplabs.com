#
# PySNMP MIB module CISCO-IP-ADDRESS-POOL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-ADDRESS-POOL-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, ModuleIdentity, NotificationType, iso, Integer32, Counter32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "iso", "Integer32", "Counter32", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpAddressPoolTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 742))
ciscoIpAddressPoolTcMIB.setRevisions(('2010-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setLastUpdated('201005030000Z')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIpAddressPoolTcMIB.setDescription('This MIB module defines textual conventions used by MIB modules defining objects describing IP address pools.')
class IpAddrPoolInstanceIdentifier(TextualConvention, Unsigned32):
    description = 'An arbitrary integer-value that uniquely identifies a row in a table defined by a MIB module defining objects describing data relating to IP address pool.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IpAddrPoolInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the IpAddressPoolIdentifier textual convention, which permits the value '0'. The use of the value '0' is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of its use."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class IpAddressPoolName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value that denotes the name assigned to an IP address pool. The semantics of the string-value are the same as those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolNameOrNull(TextualConvention, OctetString):
    description = 'This textual convention serves as an extension of the IpAddressPoolName textual convention, which permits the null string. The use of the null string is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of its use.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolGroupName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value that denotes the name assigned to an IP address pool group. The semantics of the string-value are the same as those specified by the SnmpAdminString textual convention defined by the SNMP-FRAMEWORK-MIB [RFC3411].'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class IpAddressPoolGroupNameOrNull(TextualConvention, OctetString):
    description = 'This textual convention serves as an extension of the IpAddressPoolGroupName textual convention, which permits the null string. The use of the null string is specific to an object, thus requiring the descriptive text associated with the object to describe the semantics of the its use.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class IpAddressPoolThresholdUnits(TextualConvention, Integer32):
    description = "An enumerated integer-value that denotes the units used when specifying an IP address pool threshold: 'other' The implementation of the MIB module using this textual convention does not recognize the IP address pool threshold units. 'absolute' The value of the corresponding IP address pool threshold is an absolute number of IP addresses or IP prefixes, depending on the context. 'percent' The value of the corresponding IP address pool threshold is a percentage of the total number of free and in-use IP addresses or IP prefixes contained by a pool."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("absolute", 2), ("percent", 3))

mibBuilder.exportSymbols("CISCO-IP-ADDRESS-POOL-TC-MIB", ciscoIpAddressPoolTcMIB=ciscoIpAddressPoolTcMIB, IpAddrPoolInstanceIdentifierOrZero=IpAddrPoolInstanceIdentifierOrZero, IpAddressPoolGroupNameOrNull=IpAddressPoolGroupNameOrNull, IpAddressPoolNameOrNull=IpAddressPoolNameOrNull, IpAddressPoolGroupName=IpAddressPoolGroupName, PYSNMP_MODULE_ID=ciscoIpAddressPoolTcMIB, IpAddressPoolThresholdUnits=IpAddressPoolThresholdUnits, IpAddressPoolName=IpAddressPoolName, IpAddrPoolInstanceIdentifier=IpAddrPoolInstanceIdentifier)
