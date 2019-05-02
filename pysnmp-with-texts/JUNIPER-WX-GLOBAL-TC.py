#
# PySNMP MIB module JUNIPER-WX-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-WX-GLOBAL-REG
# Produced by pysmi-0.3.4 at Wed May  1 14:01:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
jnxWxModules, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-REG", "jnxWxModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Counter64, TimeTicks, Unsigned32, Gauge32, MibIdentifier, Integer32, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxWxGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 2))
jnxWxGlobalTcModule.setRevisions(('2006-06-08 18:00', '2005-05-09 10:10', '2004-03-15 14:00', '2003-06-26 20:00', '2002-11-07 19:00', '2001-07-29 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxWxGlobalTcModule.setRevisionsDescriptions((' Update contact and MIB with Juniper information Add wxc590 and wx60 chassis type.', ' Add wxc250 chassis type.', ' Add wx100 chassis type.', ' Add wx80 chassis type.', ' Add wx20 chassis type.', ' Rev 1.0 Initial version of MIB module JUNIPER-WX-GLOBAL-TC.',))
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setOrganization('Juniper Networks, Inc')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setContactInfo(' Customer Support Juniper Networks, Inc. 1194 North Mathilda Avenue Sunnyvale, CA 94089 +1 888-314-JTAC support@juniper.net')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setDescription(" A MIB module containing textual conventions for Juniper Networks' enterprise MIB modules. These textual conventions are used across all WX products.")
class TcAppName(TextualConvention, OctetString):
    description = " Represents the name of an application. This has all the restrictions of the DisplayString textual convention with the following additional ones: - Only the following characters/character ranges are allowed: 0-9 A-Z a-z :./#$&_-+()' <space> Any object defined using this syntax may not exceed 64 characters in length."
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcQosIdentifier(TextualConvention, OctetString):
    description = " Represents the name of a QoS class, a tunnel or a tunnel ip address encoded as a string. This has all the restrictions of the DisplayString textual convention with the following additional ones: - Only the following characters/character ranges are allowed: 0-9 A-Z a-z :./#$&_-+()' <space> Any object defined using this syntax may not exceed 24 characters in length."
    status = 'current'
    displayHint = '24a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 24)

class TcChassisType(TextualConvention, Integer32):
    description = ' Enumerates all possible chassis types for WX devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("jnxWxOther", 1), ("jnxWx50", 2), ("jnxWx20", 3), ("jnxWx80", 4), ("jnxWx100", 5), ("jnxWxc500", 6), ("jnxWx15", 7), ("jnxWxc250", 8), ("jnxWx100V3", 9), ("jnxWx60", 10), ("jnxWxc590", 11), ("jnxIsm200Wxc", 12), ("jnxWxc1800", 13), ("jnxWxc2600", 14), ("jnxWxc3400", 15))

mibBuilder.exportSymbols("JUNIPER-WX-GLOBAL-TC", jnxWxGlobalTcModule=jnxWxGlobalTcModule, TcQosIdentifier=TcQosIdentifier, TcAppName=TcAppName, PYSNMP_MODULE_ID=jnxWxGlobalTcModule, TcChassisType=TcChassisType)
