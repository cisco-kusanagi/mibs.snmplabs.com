#
# PySNMP MIB module OPTIX-SONET-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-SYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
optixCommonSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommonSonet")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Integer32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, Unsigned32, NotificationType, Bits, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "Bits", "ObjectIdentity", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixSonetSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30))
optixSonetSystem.setRevisions(('2006-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: optixSonetSystem.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: optixSonetSystem.setLastUpdated('200602250000Z')
if mibBuilder.loadTexts: optixSonetSystem.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: optixSonetSystem.setContactInfo('R&D Building Huawei Technologies Co., Ltd. Bantian, Longgang District Shenzhen, P. R. China http://www.huawei.com Zip:518129 E-mail:support@huawei.com ')
if mibBuilder.loadTexts: optixSonetSystem.setDescription('Description.')
alwMsgAll = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10))
setMsgAll = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setMsgAll.setStatus('current')
if mibBuilder.loadTexts: setMsgAll.setDescription('Allow or inhibit automatic report alarms and events')
alwPMReptAll = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20))
setPMReptAll = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setPMReptAll.setStatus('current')
if mibBuilder.loadTexts: setPMReptAll.setDescription('Allow or inhibit Automatic report PM datas')
optixSonetSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30))
optixSonetSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1))
optixSonetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1, 1)).setObjects(("OPTIX-SONET-SYS-MIB", "setMsgAll"), ("OPTIX-SONET-SYS-MIB", "setPMReptAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    optixSonetObjectGroup = optixSonetObjectGroup.setStatus('current')
if mibBuilder.loadTexts: optixSonetObjectGroup.setDescription('Enter the description of the created OBJECT-GROUP.')
optixSonetSystemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2))
optixSonetBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2, 1)).setObjects(("OPTIX-SONET-SYS-MIB", "optixSonetObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    optixSonetBasicCompliance = optixSonetBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: optixSonetBasicCompliance.setDescription('Enter the description of the created MODULE-COMPLIANCE.')
mibBuilder.exportSymbols("OPTIX-SONET-SYS-MIB", setPMReptAll=setPMReptAll, optixSonetObjectGroup=optixSonetObjectGroup, setMsgAll=setMsgAll, optixSonetSystem=optixSonetSystem, optixSonetBasicCompliance=optixSonetBasicCompliance, PYSNMP_MODULE_ID=optixSonetSystem, optixSonetSystemCompliances=optixSonetSystemCompliances, alwMsgAll=alwMsgAll, alwPMReptAll=alwPMReptAll, optixSonetSystemConformance=optixSonetSystemConformance, optixSonetSystemGroups=optixSonetSystemGroups)
