#
# PySNMP MIB module Wellfleet-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-RADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:41:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, NotificationType, TimeTicks, Gauge32, Unsigned32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Bits, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "Unsigned32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Bits", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfRadiusGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfRadiusGroup")
wfRadiusTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1), )
if mibBuilder.loadTexts: wfRadiusTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusTable.setDescription('Radius slot information by the Radius Client.')
wfRadiusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1), ).setIndexNames((0, "Wellfleet-RADIUS-MIB", "wfRadiusSlot"))
if mibBuilder.loadTexts: wfRadiusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusEntry.setDescription('An entry defining RADIUS on specified slot')
wfRadiusDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusDelete.setDescription("`This value specifies if RADIUS is configured on this router. '")
wfRadiusAuthDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusAuthDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusAuthDisable.setDescription('`The value enabled specifies that RADIUS authentication is active on the router. The value disabled specifies it is configured, but has been deactivated.')
wfRadiusAcctDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusAcctDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusAcctDisable.setDescription('`The value enabled specifies that RADIUS accounting is active on the router. The value disabled specifies it is configured, but has been deactivated.')
wfRadiusSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusSlot.setDescription('The slots number configured for RADIUS authentication')
wfRadiusClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusClientIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusClientIpAddress.setDescription('A 32-bit integer specifying the IP address associated with Radius Client.')
wfRadiusAcctDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("all", 1), ("incoming", 2), ("outgoing", 3))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusAcctDirection.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusAcctDirection.setDescription('The value specifies whether a session should generate accounting request based o n the direction of the call. all- means sessions established by incoming as well as outgoing calls ma generate accounting requests. incoming- only sessions established by incoming calls may generate accounting requests. outgoing- only sessions established by outgoing calls may generate accounting requests.')
wfRadiusDebugMsgLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("three", 3), ("nodebug", 4))).clone('nodebug')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusDebugMsgLevel.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusDebugMsgLevel.setDescription('This attribute is used to assign the level of RADIUS Debug messages logged by the RADIUS client.')
wfRadiusCfgMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusCfgMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusCfgMask.setDescription('Used by SM to indicate the Radius being configured by L2TP or by Switch Service.')
wfRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2), )
if mibBuilder.loadTexts: wfRadiusServerTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerTable.setDescription('Table of servers accessible for this router.')
wfRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1), ).setIndexNames((0, "Wellfleet-RADIUS-MIB", "wfRadiusServerIpAddress"))
if mibBuilder.loadTexts: wfRadiusServerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerEntry.setDescription('')
wfRadiusServerDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerDelete.setDescription('')
wfRadiusServerDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerDisable.setDescription(' ')
wfRadiusServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusServerIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerIpAddress.setDescription('`A 32-bit integer specifying the IP address of the primary RADIUS server')
wfRadiusServerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("authonly", 1), ("acctonly", 2), ("both", 3))).clone('both')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerMode.setDescription('The server supports both authentication and accounting')
wfRadiusServerAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusServerAuthState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAuthState.setDescription('Displays the state of the Radius Server as seen by the Radius Client')
wfRadiusServerAuthUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 6), Integer32().clone(1645)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerAuthUdpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAuthUdpPort.setDescription('The UDP port of the RADIUS server')
wfRadiusServerAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("alternate", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerAuthType.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAuthType.setDescription('The server type either primary or alternate')
wfRadiusServerAcctState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusServerAcctState.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAcctState.setDescription('Displays the state of the Radius Server as seen by the Radius Client')
wfRadiusServerAcctUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 9), Integer32().clone(1646)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerAcctUdpPort.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAcctUdpPort.setDescription('The UDP port of the RADIUS accounting server')
wfRadiusServerAcctType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("alternate", 2))).clone('primary')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerAcctType.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAcctType.setDescription('The accounting server type either primary or alternate')
wfRadiusPrimarySecret = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusPrimarySecret.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusPrimarySecret.setDescription('`The secret used to communicate with the primary RADIUS server')
wfRadiusServerResponseTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerResponseTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerResponseTimeout.setDescription('The number of seconds to wait before retransmitting the request to the server')
wfRadiusServerRetryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerRetryMax.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerRetryMax.setDescription('The maximum number of times a request is retransmitted before determining the RADIUS server is unreachable')
wfRadiusServerResetTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerResetTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerResetTimer.setDescription('The number of minutes to wait before retrying the primary RADIUS sever after a failure.')
wfRadiusServerAutomaticReset = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfRadiusServerAutomaticReset.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusServerAutomaticReset.setDescription(' If enabled, automatically resets the state of the failed server to be available. Sends a test access request to the failed server at intervals configured in wfRadiusServerResetTimer and marks it available if a reply is received. If disabled, reset the state of the failed server to available after the timeout configured in wfRadiusServerResetTimer. No test access requests are sent.')
wfRadiusStatsTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3), )
if mibBuilder.loadTexts: wfRadiusStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsTable.setDescription('Table of RADIUS server statistic record.')
wfRadiusStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1), ).setIndexNames((0, "Wellfleet-RADIUS-MIB", "wfRadiusStatsSlot"), (0, "Wellfleet-RADIUS-MIB", "wfRadiusStatsIpAddress"))
if mibBuilder.loadTexts: wfRadiusStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsEntry.setDescription('')
wfRadiusStatsIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsIpAddress.setDescription('`A 32-bit integer specifying the IP address of the RADIUS server')
wfRadiusStatsSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsSlot.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsSlot.setDescription('RADIUS server statistics per slot')
wfRadiusStatsAuthReqCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthReqCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthReqCount.setDescription('Successful RADIUS Authentication request maded to this RADIUS server from this slot')
wfRadiusStatsAuthReqOutstanding = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthReqOutstanding.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthReqOutstanding.setDescription('Outstanding RADIUS Authentication request made to this RADIUS server from this slot')
wfRadiusStatsAuthRespSucc = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthRespSucc.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthRespSucc.setDescription('Successful RADIUS Authentication request maded to this RADIUS server from this slot')
wfRadiusStatsAuthRespFail = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthRespFail.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthRespFail.setDescription('Failed RADIUS Authentication request maded to this RADIUS server from this slot')
wfRadiusStatsAuthNoResp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthNoResp.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthNoResp.setDescription('No valid RADIUS Authentication response received from RADIUS server or No server available.')
wfRadiusStatsAuthRespInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthRespInvalid.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthRespInvalid.setDescription('Invalid RADIUS Authentication response received from RADIUS server on this slot')
wfRadiusStatsAuthRespTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthRespTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthRespTimeouts.setDescription('Number of Timeouts occuring to this RADIUS server from this slot')
wfRadiusStatsAuthAltServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAuthAltServerRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAuthAltServerRetries.setDescription('Number of requests for alternate RADIUS serverfrom this slot based on failure to communicate with this server')
wfRadiusStatsAcctReqStart = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctReqStart.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctReqStart.setDescription('Number of Accounting requests indicating Start of a call')
wfRadiusStatsAcctReqStop = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctReqStop.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctReqStop.setDescription('Number of Accounting requests indicating Stop of a call')
wfRadiusStatsAcctRespTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctRespTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctRespTimeouts.setDescription('Number of Accounting requests timed out waiting for response from the Accounting Server')
wfRadiusStatsAcctRespFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctRespFailed.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctRespFailed.setDescription('Number of Accounting requests that did not get a response')
wfRadiusStatsAcctAltServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctAltServerRetries.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctAltServerRetries.setDescription('Number of retries expiring causing alternate server to be used. This statistic indicates the server used as an alternate server.')
wfRadiusStatsAcctResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 22, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfRadiusStatsAcctResponse.setStatus('mandatory')
if mibBuilder.loadTexts: wfRadiusStatsAcctResponse.setDescription('Number of Accounting Responses from the Accounting server')
mibBuilder.exportSymbols("Wellfleet-RADIUS-MIB", wfRadiusServerAcctState=wfRadiusServerAcctState, wfRadiusStatsAcctRespFailed=wfRadiusStatsAcctRespFailed, wfRadiusServerAuthUdpPort=wfRadiusServerAuthUdpPort, wfRadiusStatsAcctRespTimeouts=wfRadiusStatsAcctRespTimeouts, wfRadiusServerEntry=wfRadiusServerEntry, wfRadiusPrimarySecret=wfRadiusPrimarySecret, wfRadiusServerRetryMax=wfRadiusServerRetryMax, wfRadiusStatsAuthRespSucc=wfRadiusStatsAuthRespSucc, wfRadiusStatsAcctResponse=wfRadiusStatsAcctResponse, wfRadiusServerAuthType=wfRadiusServerAuthType, wfRadiusDebugMsgLevel=wfRadiusDebugMsgLevel, wfRadiusStatsSlot=wfRadiusStatsSlot, wfRadiusStatsAuthReqOutstanding=wfRadiusStatsAuthReqOutstanding, wfRadiusServerDelete=wfRadiusServerDelete, wfRadiusStatsEntry=wfRadiusStatsEntry, wfRadiusServerIpAddress=wfRadiusServerIpAddress, wfRadiusStatsAuthRespFail=wfRadiusStatsAuthRespFail, wfRadiusClientIpAddress=wfRadiusClientIpAddress, wfRadiusServerAcctUdpPort=wfRadiusServerAcctUdpPort, wfRadiusServerAutomaticReset=wfRadiusServerAutomaticReset, wfRadiusServerAuthState=wfRadiusServerAuthState, wfRadiusStatsAcctReqStart=wfRadiusStatsAcctReqStart, wfRadiusStatsAcctAltServerRetries=wfRadiusStatsAcctAltServerRetries, wfRadiusStatsAcctReqStop=wfRadiusStatsAcctReqStop, wfRadiusServerMode=wfRadiusServerMode, wfRadiusAcctDirection=wfRadiusAcctDirection, wfRadiusEntry=wfRadiusEntry, wfRadiusStatsAuthRespInvalid=wfRadiusStatsAuthRespInvalid, wfRadiusCfgMask=wfRadiusCfgMask, wfRadiusStatsTable=wfRadiusStatsTable, wfRadiusServerResponseTimeout=wfRadiusServerResponseTimeout, wfRadiusStatsAuthRespTimeouts=wfRadiusStatsAuthRespTimeouts, wfRadiusAuthDisable=wfRadiusAuthDisable, wfRadiusStatsAuthReqCount=wfRadiusStatsAuthReqCount, wfRadiusAcctDisable=wfRadiusAcctDisable, wfRadiusSlot=wfRadiusSlot, wfRadiusStatsAuthAltServerRetries=wfRadiusStatsAuthAltServerRetries, wfRadiusServerAcctType=wfRadiusServerAcctType, wfRadiusServerResetTimer=wfRadiusServerResetTimer, wfRadiusServerTable=wfRadiusServerTable, wfRadiusStatsIpAddress=wfRadiusStatsIpAddress, wfRadiusServerDisable=wfRadiusServerDisable, wfRadiusDelete=wfRadiusDelete, wfRadiusTable=wfRadiusTable, wfRadiusStatsAuthNoResp=wfRadiusStatsAuthNoResp)
