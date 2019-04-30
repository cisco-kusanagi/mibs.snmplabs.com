#
# PySNMP MIB module CENTILLION-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, Counter64, Integer32, ModuleIdentity, NotificationType, enterprises, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "enterprises", "IpAddress", "ObjectIdentity")
Counter32, = mibBuilder.importSymbols("SNMPv2-SMI-v1", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class StatusIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class SsBackplaneType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("atmBus", 2))

class SsChassisType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("six-slot", 2), ("twelve-slot", 3), ("workgroup", 4), ("three-slotC50N", 5), ("three-slotC50T", 6), ("six-slotBH5005", 7))

class SsModuleType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50))
    namedValues = NamedValues(("empty", 1), ("other", 2), ("mTR4PC", 3), ("mTRMCP4PC", 4), ("mATM", 5), ("mTRFiber", 6), ("mTRMCPFiber", 7), ("mEther16PC10BT", 8), ("mEtherMCP8PC10BT", 9), ("mATM2PSMFiber", 10), ("mATM2PCopper", 11), ("mATM4PMMFiber", 12), ("mATM4PSMFiber", 13), ("mATM4PCopper", 14), ("mATMMCP2PSMFiber", 15), ("mATMMCP2PMMFiber", 16), ("mATMMCP2PCopper", 17), ("mATMMCP4PSMFiber", 18), ("mATMMCP4PMMFiber", 19), ("mATMMCP4PCopper", 20), ("mATM2PC", 21), ("mATM4PC", 22), ("mATMMCP2PC", 23), ("mATMMCP4PC", 24), ("mEther16P10BT100BTCopper", 25), ("mEther14P10BT100BF", 26), ("mEther8P10BF", 27), ("mEther10P10BT100BT", 28), ("mEther16P10BT100BTMixed", 29), ("mEther10P10BT100BTMIX", 30), ("mEther12PBFL", 32), ("mEther16P4x4", 33), ("mTRMCP8PC", 34), ("mTR8PC", 35), ("mEther24PC", 36), ("mEther24P10BT100BT", 37), ("mEther24P100BFx", 38), ("mTR8PFiber", 39), ("mATM4PMDA", 40), ("mATMMCP4PMDA", 41), ("mEther4P100BT", 42), ("mTR24PC", 43), ("mTR16PC", 44), ("mATMMCP1PSMFiber", 45), ("mATMMCP1PMMFiber", 46), ("mATM1PMMFiber", 47), ("mATM1PVNR", 48), ("mEther24P10BT100BTx", 49), ("mEther24P100BFX", 50))

class SsMediaType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("mediaUnkown", 1), ("mediaTokenRing", 2), ("mediaFDDI", 3), ("mediaEthernet", 4), ("mediaATM", 5))

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class Boolean(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class BitField(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("clear", 1), ("set", 2))

class PortId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class CardId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 16)

class FailIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class EnableIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

centillion = MibIdentifier((1, 3, 6, 1, 4, 1, 930))
cnProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1))
proprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2))
extensions = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3))
cnTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 4))
cnSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1))
cnATM = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2))
sysChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 1))
sysConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 2))
sysMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 3))
sysTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 4))
sysEvtLogMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 5))
atmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 1))
atmMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2))
atmLane = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 3))
atmSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 4))
sysMcpRedundTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 1))
cnPvcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 2))
cnCentillion100 = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 1))
cnIBM8251 = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 2))
cnBayStack301 = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 3))
cn5000BH_MCP = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 4)).setLabel("cn5000BH-MCP")
cnCentillion50N = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 5))
cnCentillion50T = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 6))
cn5005BH_MCP = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 1, 7)).setLabel("cn5005BH-MCP")
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 1), SsChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('mandatory')
chassisBkplType = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 2), SsBackplaneType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisBkplType.setStatus('mandatory')
chassisPs1FailStatus = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 3), FailIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs1FailStatus.setStatus('mandatory')
chassisPs2FailStatus = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 4), FailIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPs2FailStatus.setStatus('mandatory')
chassisFanFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 5), FailIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisFanFailStatus.setStatus('mandatory')
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('mandatory')
chassisPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPartNumber.setStatus('mandatory')
slotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9), )
if mibBuilder.loadTexts: slotConfigTable.setStatus('mandatory')
slotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1), ).setIndexNames((0, "CENTILLION-ROOT-MIB", "slotNumber"))
if mibBuilder.loadTexts: slotConfigEntry.setStatus('mandatory')
slotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotNumber.setStatus('mandatory')
slotModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 2), SsModuleType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleType.setStatus('deprecated')
slotModuleHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleHwVer.setStatus('mandatory')
slotModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleSerialNumber.setStatus('mandatory')
slotModuleSwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleSwVer.setStatus('mandatory')
slotModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleStatus.setStatus('mandatory')
slotModuleLeds = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleLeds.setStatus('mandatory')
slotModuleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotModuleReset.setStatus('mandatory')
slotConfigDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 9), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConfigDelete.setStatus('mandatory')
slotConfigMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 10), SsMediaType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotConfigMediaType.setStatus('mandatory')
slotModuleMaxRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleMaxRAM.setStatus('mandatory')
slotModuleInstalledRAM = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleInstalledRAM.setStatus('mandatory')
slotModuleFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleFlashSize.setStatus('mandatory')
slotModuleProductImageId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("noAtmLanEmulation", 2), ("minAtmLanEmulation", 3), ("fullAtmLanEmulation", 4), ("pnnifullAtmLanEmulation", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleProductImageId.setStatus('mandatory')
slotModuleBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 15), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotModuleBaseMacAddress.setStatus('mandatory')
slotLastResetEPC = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLastResetEPC.setStatus('mandatory')
slotLastResetVirtualAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLastResetVirtualAddress.setStatus('mandatory')
slotLastResetCause = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLastResetCause.setStatus('mandatory')
slotLastResetTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotLastResetTimeStamp.setStatus('mandatory')
slotConfigAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 20), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConfigAdd.setStatus('mandatory')
slotConfigExtClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConfigExtClockSource.setStatus('mandatory')
slotConfigTrafficShapingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 1, 1, 9, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConfigTrafficShapingRate.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-ROOT-MIB", EnableIndicator=EnableIndicator, slotNumber=slotNumber, SsChassisType=SsChassisType, SsModuleType=SsModuleType, slotLastResetEPC=slotLastResetEPC, cnPvcTraps=cnPvcTraps, slotLastResetVirtualAddress=slotLastResetVirtualAddress, sysMcpRedundTrap=sysMcpRedundTrap, sysEvtLogMgmt=sysEvtLogMgmt, CardId=CardId, chassisPs1FailStatus=chassisPs1FailStatus, cnATM=cnATM, SsMediaType=SsMediaType, slotConfigTable=slotConfigTable, slotModuleHwVer=slotModuleHwVer, slotConfigMediaType=slotConfigMediaType, cnBayStack301=cnBayStack301, SsBackplaneType=SsBackplaneType, sysConfig=sysConfig, chassisPartNumber=chassisPartNumber, slotModuleLeds=slotModuleLeds, slotConfigExtClockSource=slotConfigExtClockSource, FailIndicator=FailIndicator, proprietary=proprietary, slotModuleReset=slotModuleReset, sysChassis=sysChassis, cnIBM8251=cnIBM8251, chassisBkplType=chassisBkplType, extensions=extensions, cnCentillion50N=cnCentillion50N, slotModuleType=slotModuleType, slotModuleProductImageId=slotModuleProductImageId, atmLane=atmLane, StatusIndicator=StatusIndicator, cnSystem=cnSystem, slotConfigEntry=slotConfigEntry, BitField=BitField, cnTemporary=cnTemporary, centillion=centillion, slotModuleStatus=slotModuleStatus, cnCentillion50T=cnCentillion50T, chassisSerialNumber=chassisSerialNumber, slotModuleSerialNumber=slotModuleSerialNumber, slotModuleFlashSize=slotModuleFlashSize, slotModuleBaseMacAddress=slotModuleBaseMacAddress, slotConfigAdd=slotConfigAdd, slotConfigDelete=slotConfigDelete, Boolean=Boolean, slotLastResetTimeStamp=slotLastResetTimeStamp, chassisFanFailStatus=chassisFanFailStatus, cn5000BH_MCP=cn5000BH_MCP, slotModuleInstalledRAM=slotModuleInstalledRAM, cnProducts=cnProducts, cn5005BH_MCP=cn5005BH_MCP, PortId=PortId, slotModuleSwVer=slotModuleSwVer, slotLastResetCause=slotLastResetCause, atmConfig=atmConfig, slotModuleMaxRAM=slotModuleMaxRAM, slotConfigTrafficShapingRate=slotConfigTrafficShapingRate, cnCentillion100=cnCentillion100, sysMonitor=sysMonitor, atmMonitor=atmMonitor, chassisPs2FailStatus=chassisPs2FailStatus, sysTrap=sysTrap, atmSonet=atmSonet, chassisType=chassisType, MacAddress=MacAddress)
