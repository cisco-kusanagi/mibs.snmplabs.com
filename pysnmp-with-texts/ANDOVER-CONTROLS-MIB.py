#
# PySNMP MIB module ANDOVER-CONTROLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANDOVER-CONTROLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:11:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, ModuleIdentity, NotificationType, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32, IpAddress, Integer32, Unsigned32, Counter32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "NotificationType", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "Unsigned32", "Counter32", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
andoverControls = ModuleIdentity((1, 3, 6, 1, 4, 1, 10829))
andoverControls.setRevisions(('2002-10-30 09:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: andoverControls.setRevisionsDescriptions(('Revision 1.0',))
if mibBuilder.loadTexts: andoverControls.setLastUpdated('200210300946Z')
if mibBuilder.loadTexts: andoverControls.setOrganization('Andover Controls Corporation')
if mibBuilder.loadTexts: andoverControls.setContactInfo('Technical Support Andover Controls Corporation 300 Brickstone Square Andover, MA 01810 USA 978-470-0555')
if mibBuilder.loadTexts: andoverControls.setDescription('This is the MIB module at the top of the Andover Controls enterprise group.')
accAlarmAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 1))
if mibBuilder.loadTexts: accAlarmAgent.setStatus('deprecated')
if mibBuilder.loadTexts: accAlarmAgent.setDescription('Cyberstation alarm group witch contains information about the last alarm sent out as a trap.')
accCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 4))
if mibBuilder.loadTexts: accCommon.setStatus('current')
if mibBuilder.loadTexts: accCommon.setDescription('Group for items that may be common to more than one product. ')
accProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 5))
if mibBuilder.loadTexts: accProduct.setStatus('current')
if mibBuilder.loadTexts: accProduct.setDescription('Group for items specific to a product or family of products. Children of this node will be product families.')
accInfinetController = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 1))
accNetController = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 2))
accFrontEnd = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 5, 3))
accSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 10829, 6))
if mibBuilder.loadTexts: accSystem.setStatus('current')
if mibBuilder.loadTexts: accSystem.setDescription('Similiar to MIB-II system group, except for Andover Controls specific information about the device.')
accModel = MibScalar((1, 3, 6, 1, 4, 1, 10829, 6, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accModel.setStatus('current')
if mibBuilder.loadTexts: accModel.setDescription('Model name of this product.')
accFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 10829, 6, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: accFirmwareVersion.setDescription('Version of the firmware running on device.')
accConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7))
accGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7, 2))
accSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10829, 7, 2, 1)).setObjects(("ANDOVER-CONTROLS-MIB", "accModel"), ("ANDOVER-CONTROLS-MIB", "accFirmwareVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    accSystemGroup = accSystemGroup.setStatus('current')
if mibBuilder.loadTexts: accSystemGroup.setDescription('Description.')
accCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 10829, 7, 3))
accBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10829, 7, 3, 1)).setObjects(("ANDOVER-CONTROLS-MIB", "accSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    accBasicCompliance = accBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: accBasicCompliance.setDescription('Compliance requires these nodes.')
mibBuilder.exportSymbols("ANDOVER-CONTROLS-MIB", accSystemGroup=accSystemGroup, accProduct=accProduct, accFrontEnd=accFrontEnd, accModel=accModel, accNetController=accNetController, accFirmwareVersion=accFirmwareVersion, accCompliance=accCompliance, accConformance=accConformance, accGroups=accGroups, PYSNMP_MODULE_ID=andoverControls, accBasicCompliance=accBasicCompliance, accSystem=accSystem, accAlarmAgent=accAlarmAgent, accInfinetController=accInfinetController, andoverControls=andoverControls, accCommon=accCommon)
