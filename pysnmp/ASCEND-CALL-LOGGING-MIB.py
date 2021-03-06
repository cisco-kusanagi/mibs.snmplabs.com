#
# PySNMP MIB module ASCEND-CALL-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-CALL-LOGGING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
callLoggingGroup, = mibBuilder.importSymbols("ASCEND-MIB", "callLoggingGroup")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, ModuleIdentity, Integer32, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, MibIdentifier, Bits, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ModuleIdentity", "Integer32", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "MibIdentifier", "Bits", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
callLoggingNumServers = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callLoggingNumServers.setStatus('mandatory')
callLoggingServerTable = MibTable((1, 3, 6, 1, 4, 1, 529, 25, 2), )
if mibBuilder.loadTexts: callLoggingServerTable.setStatus('mandatory')
callLoggingServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 25, 2, 1), ).setIndexNames((0, "ASCEND-CALL-LOGGING-MIB", "callLoggingServerIndex"))
if mibBuilder.loadTexts: callLoggingServerEntry.setStatus('mandatory')
callLoggingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callLoggingServerIndex.setStatus('mandatory')
callLoggingCurrentServerFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callLoggingCurrentServerFlag.setStatus('mandatory')
callLoggingServerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingServerIPAddress.setStatus('mandatory')
callLoggingEnableActiveServer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 25, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notApplicable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingEnableActiveServer.setStatus('mandatory')
callLoggingStatus = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingStatus.setStatus('mandatory')
callLoggingPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingPortNumber.setStatus('mandatory')
callLoggingKey = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingKey.setStatus('mandatory')
callLoggingTimeout = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingTimeout.setStatus('mandatory')
callLoggingIdBase = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 10, 16))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("base10", 10), ("base16", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingIdBase.setStatus('mandatory')
callLoggingResetTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingResetTime.setStatus('mandatory')
callLoggingStopPacketsOnly = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingStopPacketsOnly.setStatus('mandatory')
callLoggingRetryLimit = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingRetryLimit.setStatus('mandatory')
callLoggingAssStatus = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("active", 2), ("aborted", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callLoggingAssStatus.setStatus('mandatory')
callLoggingDroppedPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callLoggingDroppedPacketCount.setStatus('mandatory')
callLoggingRadCompatMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 25, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("radOldAscend", 3), ("radVendorSpecific", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callLoggingRadCompatMode.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-CALL-LOGGING-MIB", callLoggingRetryLimit=callLoggingRetryLimit, callLoggingAssStatus=callLoggingAssStatus, callLoggingCurrentServerFlag=callLoggingCurrentServerFlag, callLoggingStatus=callLoggingStatus, callLoggingNumServers=callLoggingNumServers, callLoggingServerTable=callLoggingServerTable, callLoggingServerIPAddress=callLoggingServerIPAddress, callLoggingEnableActiveServer=callLoggingEnableActiveServer, callLoggingPortNumber=callLoggingPortNumber, callLoggingDroppedPacketCount=callLoggingDroppedPacketCount, callLoggingStopPacketsOnly=callLoggingStopPacketsOnly, callLoggingKey=callLoggingKey, callLoggingServerEntry=callLoggingServerEntry, callLoggingServerIndex=callLoggingServerIndex, callLoggingTimeout=callLoggingTimeout, callLoggingIdBase=callLoggingIdBase, callLoggingRadCompatMode=callLoggingRadCompatMode, callLoggingResetTime=callLoggingResetTime)
