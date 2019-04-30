#
# PySNMP MIB module CISCO-DOT11-ANTENNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-ANTENNA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Unsigned32, NotificationType, Counter64, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, IpAddress, ModuleIdentity, Bits, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Bits", "Integer32", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoDot11AntennaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 384))
ciscoDot11AntennaMIB.setRevisions(('2016-02-15 00:00', '2003-12-08 00:00',))
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setLastUpdated('201602150000Z')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setOrganization('Cisco System Inc.')
cDot11AntennaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1))
cDot11AntennaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1))
cDot11AntennaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11AntennaTable.setStatus('current')
cDot11AntennaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11AntennaEntry.setStatus('current')
cDot11AntennaIsGainConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaIsGainConfigured.setStatus('current')
cDot11AntennaResultantGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaResultantGain.setStatus('current')
cDot11AntennaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2))
cDot11AntennaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1))
cDot11AntennaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2))
cDot11AntennaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaMIBCompliance = cDot11AntennaMIBCompliance.setStatus('current')
cDot11AntennaGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaIsGainConfigured"), ("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaResultantGain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaGlobalGroup = cDot11AntennaGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-ANTENNA-MIB", cDot11AntennaResultantGain=cDot11AntennaResultantGain, cDot11AntennaTable=cDot11AntennaTable, cDot11AntennaGlobalGroup=cDot11AntennaGlobalGroup, cDot11AntennaMIBConform=cDot11AntennaMIBConform, cDot11AntennaMIBGroups=cDot11AntennaMIBGroups, cDot11AntennaEntry=cDot11AntennaEntry, ciscoDot11AntennaMIB=ciscoDot11AntennaMIB, cDot11AntennaMIBObjects=cDot11AntennaMIBObjects, cDot11AntennaGlobal=cDot11AntennaGlobal, PYSNMP_MODULE_ID=ciscoDot11AntennaMIB, cDot11AntennaMIBCompliances=cDot11AntennaMIBCompliances, cDot11AntennaIsGainConfigured=cDot11AntennaIsGainConfigured, cDot11AntennaMIBCompliance=cDot11AntennaMIBCompliance)
