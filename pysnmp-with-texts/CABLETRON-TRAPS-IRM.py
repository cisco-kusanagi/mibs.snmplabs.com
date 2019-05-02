#
# PySNMP MIB module CABLETRON-TRAPS-IRM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CABLETRON-TRAPS-IRM
# Produced by pysmi-0.3.4 at Wed May  1 11:44:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
boardIndex, boardSrcAddrLocked = mibBuilder.importSymbols("IRM3-MIB", "boardIndex", "boardSrcAddrLocked")
devTrafficThreshold, devBroadThreshold, deviceTimeBase, devErrorThreshold, deviceSrcAddrLocked, devCollsThreshold, devErrorSource = mibBuilder.importSymbols("REPEATER-MIB-2", "devTrafficThreshold", "devBroadThreshold", "deviceTimeBase", "devErrorThreshold", "deviceSrcAddrLocked", "devCollsThreshold", "devErrorSource")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, enterprises, iso, TimeTicks, ObjectIdentity, MibIdentifier, Bits, Gauge32, NotificationType, IpAddress, Integer32, NotificationType, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "enterprises", "iso", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "Gauge32", "NotificationType", "IpAddress", "Integer32", "NotificationType", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
srcAddressPortGrpLockStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,308)).setObjects(("IRM3-MIB", "boardIndex"), ("IRM3-MIB", "boardSrcAddrLocked"))
if mibBuilder.loadTexts: srcAddressPortGrpLockStatusChange.setDescription('This trap is generated when a change to the source address locking is detected at the port group level.')
deviceTrafficThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,268)).setObjects(("REPEATER-MIB-2", "devTrafficThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
if mibBuilder.loadTexts: deviceTrafficThresholdExceeded.setDescription('This trap will be generated when the traffic (good packets per time interval) has been exceed for the entire MMAC.')
deviceErrorThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,269)).setObjects(("REPEATER-MIB-2", "devErrorThreshold"), ("REPEATER-MIB-2", "devErrorSource"), ("REPEATER-MIB-2", "deviceTimeBase"))
if mibBuilder.loadTexts: deviceErrorThresholdExceeded.setDescription('This trap will be generated when packets of the selected error type exceeds a threshold percentage of the good packets for a particular interval for the entire MMAC.')
deviceCollsionThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,270)).setObjects(("REPEATER-MIB-2", "devCollsThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
if mibBuilder.loadTexts: deviceCollsionThresholdExceeded.setDescription('This trap will be generated when collsions exceed a threshold percentage of the good packets for a particular interval for the entire MMAC.')
deviceBroadcastThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,288)).setObjects(("REPEATER-MIB-2", "devBroadThreshold"), ("REPEATER-MIB-2", "deviceTimeBase"))
if mibBuilder.loadTexts: deviceBroadcastThresholdExceeded.setDescription('This trap is generated when the broadcast packets (per time interval) have exceeded the threshold for the entire MMAC.')
lockStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 52) + (0,278)).setObjects(("REPEATER-MIB-2", "deviceSrcAddrLocked"))
if mibBuilder.loadTexts: lockStatusChanged.setDescription('This trap is generated when the status of the address lock changes.')
mibBuilder.exportSymbols("CABLETRON-TRAPS-IRM", srcAddressPortGrpLockStatusChange=srcAddressPortGrpLockStatusChange, deviceErrorThresholdExceeded=deviceErrorThresholdExceeded, deviceTrafficThresholdExceeded=deviceTrafficThresholdExceeded, lockStatusChanged=lockStatusChanged, cabletron=cabletron, deviceBroadcastThresholdExceeded=deviceBroadcastThresholdExceeded, deviceCollsionThresholdExceeded=deviceCollsionThresholdExceeded)
