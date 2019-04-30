#
# PySNMP MIB module CISCO-WAN-TRAP-VARS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-TRAP-VARS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, IpAddress, Counter32, Gauge32, Unsigned32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "Gauge32", "Unsigned32", "Integer32", "iso")
DisplayString, AutonomousType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "AutonomousType", "TextualConvention")
ciscoWanTrapVarsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 5))
ciscoWanTrapVarsMIB.setRevisions(('2002-11-26 00:00', '2002-07-17 00:00', '2001-11-07 00:00', '2001-11-06 00:00', '2001-07-26 00:00', '1999-05-21 00:00',))
if mibBuilder.loadTexts: ciscoWanTrapVarsMIB.setLastUpdated('200211260000Z')
if mibBuilder.loadTexts: ciscoWanTrapVarsMIB.setOrganization('Cisco Systems, Inc.')
cwTrapVarMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 1))
cwTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1))
cwTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapIndex.setStatus('current')
cwTrapSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSlotNumber.setStatus('current')
cwTrapPhysicalVendorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalVendorType.setStatus('current')
cwTrapLineModuleNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapLineModuleNumber.setStatus('current')
cwTrapOctetString = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapOctetString.setStatus('current')
cwTrapDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapDisplayString.setStatus('current')
cwTrapPhysicalContainer = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalContainer.setStatus('current')
cwTrapPhysicalUnit = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapPhysicalUnit.setStatus('current')
cwTrapCardRole = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2), ("t3", 3), ("e3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapCardRole.setStatus('current')
cwTrapSctCardType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("axsm", 1), ("axsme", 2), ("pxm1e", 3), ("hsfr", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctCardType.setStatus('current')
cwTrapSctType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portSct", 1), ("cardSct", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctType.setStatus('current')
cwTrapSctId = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctId.setStatus('current')
cwTrapSctMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSctMajorVersion.setStatus('current')
cwTrapVarLength = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapVarLength.setStatus('current')
cwTrapAtmAddressType = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 8))).clone(namedValues=NamedValues(("e164", 3), ("nsap", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapAtmAddressType.setStatus('current')
cwTrapReference = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapReference.setStatus('current')
cwTrapSecondIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapSecondIndex.setStatus('current')
cwTrapThirdIndex = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 5, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwTrapThirdIndex.setStatus('current')
cwTrapVarsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2))
cwTrapVarsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1))
cwTrapVarsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2))
cwTrapVarsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 1)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance = cwTrapVarsCompliance.setStatus('deprecated')
cwTrapVarsCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 2)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance2 = cwTrapVarsCompliance2.setStatus('deprecated')
cwTrapVarsCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 3)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance3 = cwTrapVarsCompliance3.setStatus('deprecated')
cwTrapVarsCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 4)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance4 = cwTrapVarsCompliance4.setStatus('deprecated')
cwTrapVarsCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 1, 5)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarsTrapGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsCompliance5 = cwTrapVarsCompliance5.setStatus('current')
cwTrapVarsTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 1)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup = cwTrapVarsTrapGroup.setStatus('deprecated')
cwTrapVarsTrapGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 2)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup2 = cwTrapVarsTrapGroup2.setStatus('deprecated')
cwTrapVarsTrapGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 3)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup3 = cwTrapVarsTrapGroup3.setStatus('deprecated')
cwTrapVarsTrapGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 4)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup4 = cwTrapVarsTrapGroup4.setStatus('deprecated')
cwTrapVarsTrapGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 5, 2, 2, 5)).setObjects(("CISCO-WAN-TRAP-VARS-MIB", "cwTrapIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSlotNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalVendorType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapLineModuleNumber"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapOctetString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapDisplayString"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalContainer"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapPhysicalUnit"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapCardRole"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctCardType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctId"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSctMajorVersion"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapVarLength"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapAtmAddressType"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapReference"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapSecondIndex"), ("CISCO-WAN-TRAP-VARS-MIB", "cwTrapThirdIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwTrapVarsTrapGroup5 = cwTrapVarsTrapGroup5.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-TRAP-VARS-MIB", cwTrapVarsCompliance=cwTrapVarsCompliance, PYSNMP_MODULE_ID=ciscoWanTrapVarsMIB, cwTrapPhysicalUnit=cwTrapPhysicalUnit, cwTrapVarsCompliance4=cwTrapVarsCompliance4, cwTrapCardRole=cwTrapCardRole, cwTrapVarsTrapGroup2=cwTrapVarsTrapGroup2, cwTrapDisplayString=cwTrapDisplayString, cwTrapVarsCompliance2=cwTrapVarsCompliance2, cwTrapVarsTrapGroup3=cwTrapVarsTrapGroup3, cwTrapVarsTrapGroup=cwTrapVarsTrapGroup, cwTrapVarsCompliance3=cwTrapVarsCompliance3, cwTrapVarsCompliance5=cwTrapVarsCompliance5, cwTrapAtmAddressType=cwTrapAtmAddressType, cwTrapVarsMIBCompliances=cwTrapVarsMIBCompliances, cwTrapVarsTrapGroup4=cwTrapVarsTrapGroup4, cwTrapVarsMIBGroups=cwTrapVarsMIBGroups, cwTrapLineModuleNumber=cwTrapLineModuleNumber, cwTrapSecondIndex=cwTrapSecondIndex, cwTrapVarsMIBConformance=cwTrapVarsMIBConformance, cwTrapIndex=cwTrapIndex, cwTrapSctMajorVersion=cwTrapSctMajorVersion, ciscoWanTrapVarsMIB=ciscoWanTrapVarsMIB, cwTrapVarMIBObjects=cwTrapVarMIBObjects, cwTrapVars=cwTrapVars, cwTrapPhysicalContainer=cwTrapPhysicalContainer, cwTrapVarsTrapGroup5=cwTrapVarsTrapGroup5, cwTrapSlotNumber=cwTrapSlotNumber, cwTrapVarLength=cwTrapVarLength, cwTrapThirdIndex=cwTrapThirdIndex, cwTrapSctType=cwTrapSctType, cwTrapSctCardType=cwTrapSctCardType, cwTrapReference=cwTrapReference, cwTrapPhysicalVendorType=cwTrapPhysicalVendorType, cwTrapOctetString=cwTrapOctetString, cwTrapSctId=cwTrapSctId)
