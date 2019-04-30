#
# PySNMP MIB module OPTIX-SONET-CRS-MIB-V2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-CRS-MIB-V2
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
optixProvisionSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixProvisionSonet")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibIdentifier, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, ModuleIdentity, Counter32, Integer32, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter32", "Integer32", "iso", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixsonetCRS = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1))
if mibBuilder.loadTexts: optixsonetCRS.setLastUpdated('200605232001Z')
if mibBuilder.loadTexts: optixsonetCRS.setOrganization('Your organization')
class RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

optixsonetCrsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3), )
if mibBuilder.loadTexts: optixsonetCrsTable.setStatus('current')
optixsonetCrsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1), ).setIndexNames((0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"), (0, "OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"))
if mibBuilder.loadTexts: optixsonetCrsEntry.setStatus('current')
optixsonetCrsMod2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(9, 10, 11, 12, 13, 15, 16, 17, 21, 22))).clone(namedValues=NamedValues(("crsSTS1", 9), ("crsSTS3C", 10), ("crsSTS6C", 11), ("crsSTS9C", 12), ("crsSTS12C", 13), ("crsSTS24C", 15), ("crsSTS48C", 16), ("crsSTS192C", 17), ("crsVT1", 21), ("crsVT2", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsMod2.setStatus('current')
optixsonetCrsFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsFrom.setStatus('current')
optixsonetCrsTo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsTo.setStatus('current')
optixsonetCrsCct = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoWay", 1), ("oneWay", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsCct.setStatus('current')
optixsonetCrsCktId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsCktId.setStatus('current')
optixsonetCrsPreferredPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsPreferredPath.setStatus('current')
optixsonetCrsRDLD = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rdld", 1), ("rdldDEA", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsRDLD.setStatus('current')
optixsonetCrsActivePath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixsonetCrsActivePath.setStatus('current')
optixsonetCrsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 3, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixsonetCrsRowStatus.setStatus('current')
optixsonetCRSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4))
optixsonetCRSGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1))
currentObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 1, 1)).setObjects(("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsMod2"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsFrom"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsTo"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCct"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsCktId"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsPreferredPath"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRDLD"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsActivePath"), ("OPTIX-SONET-CRS-MIB-V2", "optixsonetCrsRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentObjectGroup = currentObjectGroup.setStatus('current')
optixsonetCRSCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2))
basicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20, 1, 4, 2, 1)).setObjects(("OPTIX-SONET-CRS-MIB-V2", "currentObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicCompliance = basicCompliance.setStatus('current')
mibBuilder.exportSymbols("OPTIX-SONET-CRS-MIB-V2", PYSNMP_MODULE_ID=optixsonetCRS, basicCompliance=basicCompliance, optixsonetCRSConformance=optixsonetCRSConformance, optixsonetCrsFrom=optixsonetCrsFrom, optixsonetCrsMod2=optixsonetCrsMod2, currentObjectGroup=currentObjectGroup, RowStatus=RowStatus, optixsonetCrsCct=optixsonetCrsCct, optixsonetCRSGroups=optixsonetCRSGroups, optixsonetCrsActivePath=optixsonetCrsActivePath, optixsonetCrsTo=optixsonetCrsTo, optixsonetCrsTable=optixsonetCrsTable, optixsonetCrsCktId=optixsonetCrsCktId, optixsonetCrsPreferredPath=optixsonetCrsPreferredPath, optixsonetCRSCompliances=optixsonetCRSCompliances, optixsonetCRS=optixsonetCRS, optixsonetCrsRDLD=optixsonetCrsRDLD, optixsonetCrsEntry=optixsonetCrsEntry, optixsonetCrsRowStatus=optixsonetCrsRowStatus)
