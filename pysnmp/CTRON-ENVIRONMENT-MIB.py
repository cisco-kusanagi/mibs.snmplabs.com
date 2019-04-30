#
# PySNMP MIB module CTRON-ENVIRONMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-ENVIRONMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ctenv, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctenv")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, TimeTicks, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "TimeTicks", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1))
boardEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2))
psEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3))
bbuEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 4))
chEnvAmbientTemp = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientTemp.setStatus('mandatory')
chEnvAmbientStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientStatus.setStatus('mandatory')
chEnvHumidity = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidity.setStatus('mandatory')
chEnvHumidityStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("dry", 2), ("normal", 3), ("moist", 4), ("inoperative", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityStatus.setStatus('mandatory')
chEnvAmbientHot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientHot.setStatus('mandatory')
chEnvAmbientWarm = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientWarm.setStatus('mandatory')
chEnvAmbientCool = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientCool.setStatus('mandatory')
chEnvAmbientCold = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvAmbientCold.setStatus('mandatory')
chEnvHumidityMoist = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityMoist.setStatus('mandatory')
chEnvHumidityDry = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvHumidityDry.setStatus('mandatory')
chEnvNumFans = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvNumFans.setStatus('mandatory')
chEnvFanTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12), )
if mibBuilder.loadTexts: chEnvFanTable.setStatus('mandatory')
chEnvFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "chEnvFanID"))
if mibBuilder.loadTexts: chEnvFanEntry.setStatus('mandatory')
chEnvFanID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanID.setStatus('mandatory')
chEnvFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("testing", 3), ("slow", 4), ("inoperative", 5), ("off", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanStatus.setStatus('mandatory')
chEnvFanAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoMode", 1), ("fullSpeed", 2), ("testingMode", 3))).clone('autoMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chEnvFanAdmin.setStatus('mandatory')
chEnvFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 1, 12, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chEnvFanSpeed.setStatus('mandatory')
boardEnvSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1), )
if mibBuilder.loadTexts: boardEnvSlotTable.setStatus('mandatory')
boardEnvSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "boardEnvSlotID"))
if mibBuilder.loadTexts: boardEnvSlotEntry.setStatus('mandatory')
boardEnvSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvSlotID.setStatus('mandatory')
boardEnvTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTemp.setStatus('mandatory')
boardEnvTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempStatus.setStatus('mandatory')
boardEnvTempRelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("warm", 3), ("hot", 4), ("inoperative", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelStatus.setStatus('mandatory')
boardEnvShutdownAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardEnvShutdownAdmin.setStatus('mandatory')
boardEnvTempHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempHot.setStatus('mandatory')
boardEnvTempWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempWarm.setStatus('mandatory')
boardEnvTempCool = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempCool.setStatus('mandatory')
boardEnvTempCold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempCold.setStatus('mandatory')
boardEnvTempRelHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelHot.setStatus('mandatory')
boardEnvTempRelWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempRelWarm.setStatus('mandatory')
boardEnvTempMaxFanRelHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempMaxFanRelHot.setStatus('mandatory')
boardEnvTempMaxFanRelWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardEnvTempMaxFanRelWarm.setStatus('mandatory')
psEnvSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1), )
if mibBuilder.loadTexts: psEnvSlotTable.setStatus('mandatory')
psEnvSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1), ).setIndexNames((0, "CTRON-ENVIRONMENT-MIB", "psEnvSlotID"))
if mibBuilder.loadTexts: psEnvSlotEntry.setStatus('mandatory')
psEnvSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvSlotID.setStatus('mandatory')
psEnvTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTemp.setStatus('mandatory')
psEnvTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("cold", 2), ("cool", 3), ("normal", 4), ("warm", 5), ("hot", 6), ("inoperative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempStatus.setStatus('mandatory')
psEnvTempHot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempHot.setStatus('mandatory')
psEnvTempWarm = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempWarm.setStatus('mandatory')
psEnvTempCool = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempCool.setStatus('mandatory')
psEnvTempCold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvTempCold.setStatus('mandatory')
psEnvFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("normal", 2), ("testing", 3), ("slow", 4), ("inoperative", 5), ("off", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvFanStatus.setStatus('mandatory')
psEnvFanAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("autoMode", 1), ("fullSpeed", 2), ("testingMode", 3))).clone('autoMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psEnvFanAdmin.setStatus('mandatory')
psEnvFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psEnvFanSpeed.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ENVIRONMENT-MIB", chEnv=chEnv, psEnvSlotTable=psEnvSlotTable, chEnvFanID=chEnvFanID, chEnvHumidityDry=chEnvHumidityDry, chEnvAmbientCool=chEnvAmbientCool, chEnvHumidityMoist=chEnvHumidityMoist, boardEnvTempRelHot=boardEnvTempRelHot, psEnvTempWarm=psEnvTempWarm, psEnvTempCold=psEnvTempCold, psEnvSlotID=psEnvSlotID, boardEnvTempHot=boardEnvTempHot, boardEnvTempWarm=boardEnvTempWarm, psEnvTempCool=psEnvTempCool, boardEnvSlotTable=boardEnvSlotTable, boardEnvTempCold=boardEnvTempCold, chEnvFanStatus=chEnvFanStatus, boardEnvSlotEntry=boardEnvSlotEntry, psEnv=psEnv, boardEnvTempMaxFanRelHot=boardEnvTempMaxFanRelHot, chEnvFanAdmin=chEnvFanAdmin, chEnvAmbientStatus=chEnvAmbientStatus, chEnvFanSpeed=chEnvFanSpeed, bbuEnv=bbuEnv, chEnvAmbientWarm=chEnvAmbientWarm, boardEnvTempMaxFanRelWarm=boardEnvTempMaxFanRelWarm, boardEnv=boardEnv, chEnvHumidity=chEnvHumidity, boardEnvTempStatus=boardEnvTempStatus, chEnvNumFans=chEnvNumFans, chEnvHumidityStatus=chEnvHumidityStatus, chEnvFanEntry=chEnvFanEntry, psEnvFanSpeed=psEnvFanSpeed, psEnvTemp=psEnvTemp, chEnvAmbientHot=chEnvAmbientHot, psEnvSlotEntry=psEnvSlotEntry, psEnvTempHot=psEnvTempHot, boardEnvTempRelWarm=boardEnvTempRelWarm, boardEnvTempCool=boardEnvTempCool, boardEnvShutdownAdmin=boardEnvShutdownAdmin, chEnvFanTable=chEnvFanTable, psEnvFanAdmin=psEnvFanAdmin, boardEnvSlotID=boardEnvSlotID, psEnvTempStatus=psEnvTempStatus, psEnvFanStatus=psEnvFanStatus, boardEnvTemp=boardEnvTemp, chEnvAmbientCold=chEnvAmbientCold, chEnvAmbientTemp=chEnvAmbientTemp, boardEnvTempRelStatus=boardEnvTempRelStatus)