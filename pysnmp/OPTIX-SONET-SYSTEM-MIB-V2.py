#
# PySNMP MIB module OPTIX-SONET-SYSTEM-MIB-V2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-SYSTEM-MIB-V2
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
optixProvisionSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixProvisionSonet")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, iso, NotificationType, ModuleIdentity, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, Bits, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "NotificationType", "ModuleIdentity", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "Bits", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
optixsonetSysAttribute = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4))
if mibBuilder.loadTexts: optixsonetSysAttribute.setLastUpdated('200605232007Z')
if mibBuilder.loadTexts: optixsonetSysAttribute.setOrganization('Your organization')
optixsonetNeType = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1))
optixsonetVendId = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetVendId.setStatus('current')
optixsonetDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetDeviceType.setStatus('current')
optixsonetEquipType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetEquipType.setStatus('current')
optixsonetNeVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetNeVersion.setStatus('current')
optixsonetSysAttributeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2))
optixsonetSysAttributeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 1))
currentObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 1, 1)).setObjects(("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetVendId"), ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetDeviceType"), ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetEquipType"), ("OPTIX-SONET-SYSTEM-MIB-V2", "optixsonetNeVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentObjectGroup = currentObjectGroup.setStatus('current')
optixsonetSysAttributeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 2))
basicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 4, 2, 2, 1)).setObjects(("OPTIX-SONET-SYSTEM-MIB-V2", "currentObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicCompliance = basicCompliance.setStatus('current')
mibBuilder.exportSymbols("OPTIX-SONET-SYSTEM-MIB-V2", PYSNMP_MODULE_ID=optixsonetSysAttribute, currentObjectGroup=currentObjectGroup, optixsonetEquipType=optixsonetEquipType, optixsonetVendId=optixsonetVendId, optixsonetSysAttribute=optixsonetSysAttribute, optixsonetNeVersion=optixsonetNeVersion, optixsonetSysAttributeConformance=optixsonetSysAttributeConformance, optixsonetSysAttributeGroups=optixsonetSysAttributeGroups, optixsonetDeviceType=optixsonetDeviceType, optixsonetNeType=optixsonetNeType, optixsonetSysAttributeCompliances=optixsonetSysAttributeCompliances, basicCompliance=basicCompliance)
