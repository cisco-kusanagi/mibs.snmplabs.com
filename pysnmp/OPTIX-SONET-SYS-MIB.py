#
# PySNMP MIB module OPTIX-SONET-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-SYS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
optixCommonSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommonSonet")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, TimeTicks, Unsigned32, Integer32, ModuleIdentity, iso, NotificationType, Gauge32, MibIdentifier, ObjectIdentity, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "iso", "NotificationType", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
optixSonetSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30))
optixSonetSystem.setRevisions(('2006-02-25 00:00',))
if mibBuilder.loadTexts: optixSonetSystem.setLastUpdated('200602250000Z')
if mibBuilder.loadTexts: optixSonetSystem.setOrganization('Huawei Technologies co.,Ltd.')
alwMsgAll = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10))
setMsgAll = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setMsgAll.setStatus('current')
alwPMReptAll = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20))
setPMReptAll = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 20, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: setPMReptAll.setStatus('current')
optixSonetSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30))
optixSonetSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1))
optixSonetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 1, 1)).setObjects(("OPTIX-SONET-SYS-MIB", "setMsgAll"), ("OPTIX-SONET-SYS-MIB", "setPMReptAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    optixSonetObjectGroup = optixSonetObjectGroup.setStatus('current')
optixSonetSystemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2))
optixSonetBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 30, 30, 2, 1)).setObjects(("OPTIX-SONET-SYS-MIB", "optixSonetObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    optixSonetBasicCompliance = optixSonetBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("OPTIX-SONET-SYS-MIB", optixSonetObjectGroup=optixSonetObjectGroup, optixSonetSystemConformance=optixSonetSystemConformance, optixSonetSystemGroups=optixSonetSystemGroups, optixSonetSystemCompliances=optixSonetSystemCompliances, alwPMReptAll=alwPMReptAll, setPMReptAll=setPMReptAll, setMsgAll=setMsgAll, alwMsgAll=alwMsgAll, optixSonetBasicCompliance=optixSonetBasicCompliance, PYSNMP_MODULE_ID=optixSonetSystem, optixSonetSystem=optixSonetSystem)
