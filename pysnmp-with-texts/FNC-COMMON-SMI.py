#
# PySNMP MIB module FNC-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FNC-COMMON-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:14:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, iso, ModuleIdentity, TimeTicks, NotificationType, Gauge32, Bits, Counter64, ObjectIdentity, IpAddress, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "Bits", "Counter64", "ObjectIdentity", "IpAddress", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fnc = ModuleIdentity((1, 3, 6, 1, 4, 1, 3861))
fnc.setRevisions(('2004-01-28 15:00', '2003-10-06 15:00', '2003-08-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fnc.setRevisionsDescriptions(('Removed conflicting NETSMART OID definitions.', 'Added FNC common MIB revision history.', 'Initial revision proposed by FW7500 and FW4020 snmp team.',))
if mibBuilder.loadTexts: fnc.setLastUpdated('200401281500Z')
if mibBuilder.loadTexts: fnc.setOrganization('Fujitsu Network Communications')
if mibBuilder.loadTexts: fnc.setContactInfo('Fujitsu Technical Assistance Center (FTAC), 1-800-USE-FTAC (1-800-873-3822)')
if mibBuilder.loadTexts: fnc.setDescription('This MIB module contains all of the base level headers used for control of the FNC enterprises MIB tree. It should contain both object definitions for specific groups and references to other objects that are contained in other MIB modules. The main utility of this MIB module is to collect the MIB tree of the base objects in the fnc branch.')
fncTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 0))
fastlane = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 1))
flash = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 2))
flashBase = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 2, 1))
stm = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 2, 1, 7))
sonet = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 2, 1, 7, 1))
flashwave = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3))
fwCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 1))
fw4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 4100))
fw4300 = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 4300))
fw4500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 4500))
fw7500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 7500))
fw4020 = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 3, 4020))
netsmart = MibIdentifier((1, 3, 6, 1, 4, 1, 3861, 4))
mibBuilder.exportSymbols("FNC-COMMON-SMI", fw4100=fw4100, PYSNMP_MODULE_ID=fnc, netsmart=netsmart, sonet=sonet, fw4300=fw4300, flashwave=flashwave, fw4020=fw4020, flashBase=flashBase, fncTraps=fncTraps, flash=flash, fnc=fnc, fastlane=fastlane, fwCommon=fwCommon, stm=stm, fw4500=fw4500, fw7500=fw7500)
