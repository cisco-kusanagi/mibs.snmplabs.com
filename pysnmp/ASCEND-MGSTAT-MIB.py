#
# PySNMP MIB module ASCEND-MGSTAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MGSTAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
mgGroup, = mibBuilder.importSymbols("ASCEND-MIB", "mgGroup")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, TimeTicks, Bits, Counter64, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Gauge32, NotificationType, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Gauge32", "NotificationType", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mgNumLinks = MibScalar((1, 3, 6, 1, 4, 1, 529, 29, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumLinks.setStatus('mandatory')
mgTable = MibTable((1, 3, 6, 1, 4, 1, 529, 29, 2), )
if mibBuilder.loadTexts: mgTable.setStatus('mandatory')
mgTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 29, 2, 1), ).setIndexNames((0, "ASCEND-MGSTAT-MIB", "mgLinkName"))
if mibBuilder.loadTexts: mgTableEntry.setStatus('mandatory')
mgLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgLinkName.setStatus('mandatory')
mgProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("asgcp", 3), ("ipdc", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgProtocol.setStatus('mandatory')
mgAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgAdminStatus.setStatus('mandatory')
mgOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgOperStatus.setStatus('mandatory')
mgLastStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgLastStatusChange.setStatus('mandatory')
mgNumInMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumInMessages.setStatus('mandatory')
mgNumInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumInOctets.setStatus('mandatory')
mgNumOutMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumOutMessages.setStatus('mandatory')
mgNumOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumOutOctets.setStatus('mandatory')
mgNumErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumErrors.setStatus('mandatory')
mgNumTimerRecovery = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgNumTimerRecovery.setStatus('mandatory')
mgTransportNumLosses = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgTransportNumLosses.setStatus('mandatory')
mgTransportNumSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgTransportNumSwitchover.setStatus('mandatory')
mgTransportTotalNumAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgTransportTotalNumAlarms.setStatus('mandatory')
mgTransportLastEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("linkUp", 3), ("linkLoss", 4), ("persistentError", 5), ("linkShutdown", 6), ("switchOver", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgTransportLastEvent.setStatus('mandatory')
mgTransportLastEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgTransportLastEventTime.setStatus('mandatory')
mgResetStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("other", 2), ("reset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgResetStatistics.setStatus('mandatory')
mgLastStatisticsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 18), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgLastStatisticsReset.setStatus('mandatory')
mgControllerTable = MibTable((1, 3, 6, 1, 4, 1, 529, 29, 3), )
if mibBuilder.loadTexts: mgControllerTable.setStatus('mandatory')
mgControllerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 29, 3, 1), ).setIndexNames((0, "ASCEND-MGSTAT-MIB", "mgControllerLinkName"), (0, "ASCEND-MGSTAT-MIB", "mgControllerIndex"))
if mibBuilder.loadTexts: mgControllerEntry.setStatus('mandatory')
mgControllerLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgControllerLinkName.setStatus('mandatory')
mgControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgControllerIndex.setStatus('mandatory')
mgControllerIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgControllerIPAddress.setStatus('mandatory')
mgControllerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgControllerPort.setStatus('mandatory')
mgControllerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgControllerOperStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MGSTAT-MIB", mgTransportNumLosses=mgTransportNumLosses, mgNumErrors=mgNumErrors, mgTableEntry=mgTableEntry, mgTransportLastEvent=mgTransportLastEvent, mgTransportLastEventTime=mgTransportLastEventTime, mgTransportNumSwitchover=mgTransportNumSwitchover, mgNumInMessages=mgNumInMessages, mgNumLinks=mgNumLinks, mgNumTimerRecovery=mgNumTimerRecovery, mgLinkName=mgLinkName, mgAdminStatus=mgAdminStatus, mgTable=mgTable, mgLastStatisticsReset=mgLastStatisticsReset, mgResetStatistics=mgResetStatistics, mgNumOutOctets=mgNumOutOctets, mgControllerOperStatus=mgControllerOperStatus, mgControllerEntry=mgControllerEntry, mgNumOutMessages=mgNumOutMessages, mgControllerIndex=mgControllerIndex, mgNumInOctets=mgNumInOctets, mgTransportTotalNumAlarms=mgTransportTotalNumAlarms, mgProtocol=mgProtocol, mgControllerTable=mgControllerTable, mgControllerIPAddress=mgControllerIPAddress, mgControllerLinkName=mgControllerLinkName, mgOperStatus=mgOperStatus, mgControllerPort=mgControllerPort, mgLastStatusChange=mgLastStatusChange)
