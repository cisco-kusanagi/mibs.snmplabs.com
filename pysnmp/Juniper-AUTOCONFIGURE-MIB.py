#
# PySNMP MIB module Juniper-AUTOCONFIGURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-AUTOCONFIGURE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:50:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Bits, MibIdentifier, Counter32, ObjectIdentity, NotificationType, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
juniAutoConfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48))
juniAutoConfMIB.setRevisions(('2004-07-26 19:54', '2002-11-22 16:08', '2002-11-22 15:24', '2000-11-16 00:00',))
if mibBuilder.loadTexts: juniAutoConfMIB.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAutoConfMIB.setOrganization('Juniper Networks')
class JuniAutoConfEncaps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19))

juniAutoConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1))
juniAutoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1))
juniAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1), )
if mibBuilder.loadTexts: juniAutoConfTable.setStatus('current')
juniAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfIfIndex"), (0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEncaps"))
if mibBuilder.loadTexts: juniAutoConfEntry.setStatus('current')
juniAutoConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniAutoConfIfIndex.setStatus('current')
juniAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2), JuniAutoConfEncaps())
if mibBuilder.loadTexts: juniAutoConfEncaps.setStatus('current')
juniAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfEnable.setStatus('current')
juniAutoConfLockoutSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutSupported.setStatus('current')
juniAutoConfLockoutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMin.setStatus('current')
juniAutoConfLockoutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMax.setStatus('current')
juniAutoConfLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutTime.setStatus('current')
juniAutoConfLockoutElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutElapsedTime.setStatus('current')
juniAutoConfNextLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfNextLockoutTime.setStatus('current')
juniAutoConfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4))
juniAutoConfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1))
juniAutoConfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2))
juniAutoConfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance = juniAutoConfCompliance.setStatus('obsolete')
juniAutoConfCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance2 = juniAutoConfCompliance2.setStatus('current')
juniAutoConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup = juniAutoConfGroup.setStatus('obsolete')
juniAutoConfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutSupported"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMin"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMax"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutElapsedTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfNextLockoutTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup2 = juniAutoConfGroup2.setStatus('current')
mibBuilder.exportSymbols("Juniper-AUTOCONFIGURE-MIB", juniAutoConfLockoutMax=juniAutoConfLockoutMax, JuniAutoConfEncaps=JuniAutoConfEncaps, juniAutoConfObjects=juniAutoConfObjects, juniAutoConfNextLockoutTime=juniAutoConfNextLockoutTime, juniAutoConfMIBGroups=juniAutoConfMIBGroups, juniAutoConfCompliance2=juniAutoConfCompliance2, PYSNMP_MODULE_ID=juniAutoConfMIB, juniAutoConfEncaps=juniAutoConfEncaps, juniAutoConfLockoutSupported=juniAutoConfLockoutSupported, juniAutoConfEnable=juniAutoConfEnable, juniAutoConfGroup2=juniAutoConfGroup2, juniAutoConfCompliance=juniAutoConfCompliance, juniAutoConfLockoutTime=juniAutoConfLockoutTime, juniAutoConfMIBConformance=juniAutoConfMIBConformance, juniAutoConfGroup=juniAutoConfGroup, juniAutoConfEntry=juniAutoConfEntry, juniAutoConf=juniAutoConf, juniAutoConfTable=juniAutoConfTable, juniAutoConfIfIndex=juniAutoConfIfIndex, juniAutoConfLockoutMin=juniAutoConfLockoutMin, juniAutoConfLockoutElapsedTime=juniAutoConfLockoutElapsedTime, juniAutoConfMIBCompliances=juniAutoConfMIBCompliances, juniAutoConfMIB=juniAutoConfMIB)
