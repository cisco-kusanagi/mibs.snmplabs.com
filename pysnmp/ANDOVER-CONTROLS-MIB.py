#
# PySNMP MIB module ANDOVER-CONTROLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANDOVER-CONTROLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:56:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, NotificationType, Integer32, Unsigned32, iso, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Unsigned32", "iso", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
andoverControls = ModuleIdentity((1, 3, 6, 1, 4, 1, 10829))
andoverControls.setRevisions(('2002-10-30 09:46',))
if mibBuilder.loadTexts: andoverControls.setLastUpdated('200210300946Z')
if mibBuilder.loadTexts: andoverControls.setOrganization('Andover Controls Corporation')
accAlarmAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 1))
if mibBuilder.loadTexts: accAlarmAgent.setStatus('deprecated')
accCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 4))
if mibBuilder.loadTexts: accCommon.setStatus('current')
accProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 5))
if mibBuilder.loadTexts: accProduct.setStatus('current')
accInfinetController = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 1))
accNetController = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 2))
accFrontEnd = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 3))
accSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 6))
if mibBuilder.loadTexts: accSystem.setStatus('current')
accModel = MibScalar((1, 3, 6, 1, 4, 1, 10829, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accModel.setStatus('current')
accFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 10829, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accFirmwareVersion.setStatus('current')
accConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7))
accGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7, 2))
accSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10829, 7, 2, 1)).setObjects(("ANDOVER-CONTROLS-MIB", "accModel"), ("ANDOVER-CONTROLS-MIB", "accFirmwareVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    accSystemGroup = accSystemGroup.setStatus('current')
accCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7, 3))
accBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10829, 7, 3, 1)).setObjects(("ANDOVER-CONTROLS-MIB", "accSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    accBasicCompliance = accBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("ANDOVER-CONTROLS-MIB", accModel=accModel, andoverControls=andoverControls, accNetController=accNetController, accSystemGroup=accSystemGroup, accCompliance=accCompliance, accAlarmAgent=accAlarmAgent, accFirmwareVersion=accFirmwareVersion, accConformance=accConformance, accCommon=accCommon, accFrontEnd=accFrontEnd, accSystem=accSystem, accInfinetController=accInfinetController, accGroups=accGroups, accBasicCompliance=accBasicCompliance, accProduct=accProduct, PYSNMP_MODULE_ID=andoverControls)
