#
# PySNMP MIB module CISCO-MGX82XX-PXM-CLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX82XX-PXM-CLOCK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Unsigned32, Counter32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Gauge32, TimeTicks, ModuleIdentity, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Gauge32", "TimeTicks", "ModuleIdentity", "IpAddress", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxPxmClockMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 72))
ciscoMgx82xxPxmClockMIB.setRevisions(('2003-05-27 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setLastUpdated('200305270000Z')
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setOrganization('Cisco Systems, Inc.')
class CmpClockConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rj45Type", 1), ("smbType", 2))

class CmpClockSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("pxmInbandClock1", 1), ("pxmServiceModuleClock1", 2), ("pxmTopSRMClock", 3), ("pxmExternalClock", 4), ("pxmInbandClock2", 5), ("pxmServiceModuleClock2", 6), ("pxmBottomSRMClock", 7), ("pxmInternalOscillator", 8), ("pxmExternalClock2", 9))

class CmpCurrentClock(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("primary", 1), ("secondary", 2), ("intOscillator", 3))

class CmpClockExistence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("clkNotPresent", 1), ("clkPresent", 2))

class CmpClockImpedance(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ohms75", 1), ("ohms100", 2), ("ohms120", 3))

pxmClockConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 16))
pxmPrimaryMuxClockSource = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 1), CmpClockSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimaryMuxClockSource.setStatus('current')
pxmPrimaryInbandClockSourceLineNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimaryInbandClockSourceLineNumber.setStatus('current')
pxmPrimarySMClockSourceSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimarySMClockSourceSlotNumber.setStatus('current')
pxmSecondaryMuxClockSource = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 4), CmpClockSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondaryMuxClockSource.setStatus('current')
pxmSecondaryInbandClockSourceLineNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondaryInbandClockSourceLineNumber.setStatus('current')
pxmSecondarySMClockSourceSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondarySMClockSourceSlotNumber.setStatus('current')
pxmCurrentClock = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 7), CmpCurrentClock()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmCurrentClock.setStatus('current')
pxmPreviousClock = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 8), CmpCurrentClock()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPreviousClock.setStatus('current')
pxmExtClockPresent = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 9), CmpClockExistence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClockPresent.setStatus('current')
pxmExtClkSrcImpedance = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 10), CmpClockImpedance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClkSrcImpedance.setStatus('current')
pxmExtClkConnectorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 11), CmpClockConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClkConnectorType.setStatus('current')
pxmClkStratumLevel = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("stratumUnknown", 1), ("stratumLevel1", 2), ("stratumLevel2", 3), ("stratumLevel3E", 4), ("stratumLevel3", 5), ("stratumLevel4", 6), ("stratumLevel4E", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmClkStratumLevel.setStatus('current')
pxmClkErrReason = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("goodClk", 1), ("unknownReason", 2), ("noClkSignal", 3), ("freqTooHigh", 4), ("freqTooLow", 5), ("excessiveJitter", 6), ("missingCard", 7), ("missingLogicalIf", 8), ("noClock", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmClkErrReason.setStatus('current')
pxmExtClock2Present = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 14), CmpClockExistence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClock2Present.setStatus('current')
pxmExtClk2SrcImpedance = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 15), CmpClockImpedance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClk2SrcImpedance.setStatus('current')
pxmExtClk2ConnectorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 16), CmpClockConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClk2ConnectorType.setStatus('current')
cmpClockMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2))
cmpClockMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1))
cmpClockMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2))
cmpClockCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2, 1)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpPrimaryClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpSecondaryClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpExtClockInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpClockCompliance = cmpClockCompliance.setStatus('current')
cmpClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 1)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmCurrentClock"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPreviousClock"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkStratumLevel"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkErrReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpClockInfoGroup = cmpClockInfoGroup.setStatus('current')
cmpPrimaryClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 2)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryMuxClockSource"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryInbandClockSourceLineNumber"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimarySMClockSourceSlotNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpPrimaryClockInfoGroup = cmpPrimaryClockInfoGroup.setStatus('current')
cmpSecondaryClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 3)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryMuxClockSource"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryInbandClockSourceLineNumber"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondarySMClockSourceSlotNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpSecondaryClockInfoGroup = cmpSecondaryClockInfoGroup.setStatus('current')
cmpExtClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 4)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClockPresent"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkSrcImpedance"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkConnectorType"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClock2Present"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2SrcImpedance"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2ConnectorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpExtClockInfoGroup = cmpExtClockInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-PXM-CLOCK-MIB", pxmExtClkConnectorType=pxmExtClkConnectorType, ciscoMgx82xxPxmClockMIB=ciscoMgx82xxPxmClockMIB, cmpClockMIBCompliances=cmpClockMIBCompliances, pxmClockConfig=pxmClockConfig, pxmExtClockPresent=pxmExtClockPresent, cmpSecondaryClockInfoGroup=cmpSecondaryClockInfoGroup, CmpCurrentClock=CmpCurrentClock, pxmExtClkSrcImpedance=pxmExtClkSrcImpedance, pxmSecondarySMClockSourceSlotNumber=pxmSecondarySMClockSourceSlotNumber, pxmPreviousClock=pxmPreviousClock, pxmExtClk2ConnectorType=pxmExtClk2ConnectorType, CmpClockConnectorType=CmpClockConnectorType, cmpClockMIBConformance=cmpClockMIBConformance, pxmClkErrReason=pxmClkErrReason, CmpClockExistence=CmpClockExistence, pxmClkStratumLevel=pxmClkStratumLevel, pxmExtClock2Present=pxmExtClock2Present, cmpClockInfoGroup=cmpClockInfoGroup, pxmPrimaryMuxClockSource=pxmPrimaryMuxClockSource, cmpExtClockInfoGroup=cmpExtClockInfoGroup, pxmSecondaryInbandClockSourceLineNumber=pxmSecondaryInbandClockSourceLineNumber, PYSNMP_MODULE_ID=ciscoMgx82xxPxmClockMIB, pxmSecondaryMuxClockSource=pxmSecondaryMuxClockSource, pxmPrimarySMClockSourceSlotNumber=pxmPrimarySMClockSourceSlotNumber, cmpClockCompliance=cmpClockCompliance, cmpClockMIBGroups=cmpClockMIBGroups, CmpClockSourceType=CmpClockSourceType, CmpClockImpedance=CmpClockImpedance, pxmCurrentClock=pxmCurrentClock, pxmExtClk2SrcImpedance=pxmExtClk2SrcImpedance, pxmPrimaryInbandClockSourceLineNumber=pxmPrimaryInbandClockSourceLineNumber, cmpPrimaryClockInfoGroup=cmpPrimaryClockInfoGroup)
