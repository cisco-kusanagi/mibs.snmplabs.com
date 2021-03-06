#
# PySNMP MIB module GWPAGERMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWPAGERMIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, ObjectIdentity, IpAddress, iso, Integer32, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, NotificationType, Gauge32, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress", "iso", "Integer32", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "NotificationType", "Gauge32", "Bits", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
gateways = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwPAGER = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43))
gwPAGERInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43, 1))
gwPAGERTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 43, 2))
gwPAGERGatewayName = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERGatewayName.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERGatewayName.setDescription('The GroupWise PAGER Gateway name.')
gwPAGERUptime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERUptime.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERUptime.setDescription('Uptime of the GroupWise PAGER Gateway.')
gwPAGERGroupWiseLink = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERGroupWiseLink.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERGroupWiseLink.setDescription('GroupWise PAGER Gateway Link: UP or DOWN')
gwPAGERFrgnLink = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERFrgnLink.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERFrgnLink.setDescription('GroupWise PAGER Gateway Foreign Link: UP or DOWN')
gwPAGEROutBytes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutBytes.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGEROutBytes.setDescription('The number of message bytes sent to GroupWise PAGER.')
gwPAGERInBytes = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInBytes.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERInBytes.setDescription('The number of message bytes received from GroupWise PAGER.')
gwPAGEROutMsgs = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGEROutMsgs.setDescription('The number of messages sent to GroupWise PAGER.')
gwPAGERInMsgs = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInMsgs.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERInMsgs.setDescription('The number of messages received from PAGER.')
gwPAGEROutStatuses = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutStatuses.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGEROutStatuses.setDescription('The number of statuses sent to PAGER.')
gwPAGERInStatuses = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInStatuses.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERInStatuses.setDescription('The number of statuses received from PAGER.')
gwPAGEROutErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGEROutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGEROutErrors.setDescription('The number of failed transfers to PAGER.')
gwPAGERInErrors = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwPAGERInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERInErrors.setDescription('The number of failed transfers from PAGER.')
gwPAGERTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 43, 2, 1), Integer32())
if mibBuilder.loadTexts: gwPAGERTrapTime.setStatus('mandatory')
if mibBuilder.loadTexts: gwPAGERTrapTime.setDescription('The time the trap occurred. Seconds since Jan 1, 1970 (GMT)')
gwPAGERStartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,1)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
if mibBuilder.loadTexts: gwPAGERStartTrap.setDescription('GroupWise PAGER Gateway start.')
gwPAGERStopTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,2)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
if mibBuilder.loadTexts: gwPAGERStopTrap.setDescription('GroupWise PAGER Gateway stop.')
gwPAGERRestartTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,3)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
if mibBuilder.loadTexts: gwPAGERRestartTrap.setDescription('GroupWise PAGER Gateway restart.')
gwPAGERGroupWiseLinkTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,4)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
if mibBuilder.loadTexts: gwPAGERGroupWiseLinkTrap.setDescription('GroupWise Link lost by GroupWise PAGER Gateway')
gwPAGERFgnLinkTrap = NotificationType((1, 3, 6, 1, 4, 1, 23, 2, 43, 1) + (0,5)).setObjects(("GWPAGERMIB", "gwPAGERTrapTime"), ("GWPAGERMIB", "gwPAGERGatewayName"))
if mibBuilder.loadTexts: gwPAGERFgnLinkTrap.setDescription('PAGER Link lost by GroupWise PAGER Gateway')
mibBuilder.exportSymbols("GWPAGERMIB", gwPAGERTrapInfo=gwPAGERTrapInfo, gwPAGERRestartTrap=gwPAGERRestartTrap, gwPAGERInBytes=gwPAGERInBytes, gwPAGERInfo=gwPAGERInfo, gwPAGERGroupWiseLinkTrap=gwPAGERGroupWiseLinkTrap, novell=novell, gwPAGERInMsgs=gwPAGERInMsgs, gwPAGERTrapTime=gwPAGERTrapTime, gwPAGERInErrors=gwPAGERInErrors, gwPAGERFrgnLink=gwPAGERFrgnLink, gwPAGERUptime=gwPAGERUptime, gwPAGEROutBytes=gwPAGEROutBytes, gwPAGERStartTrap=gwPAGERStartTrap, gwPAGEROutErrors=gwPAGEROutErrors, gwPAGERGatewayName=gwPAGERGatewayName, gwPAGEROutMsgs=gwPAGEROutMsgs, gwPAGER=gwPAGER, gwPAGERGroupWiseLink=gwPAGERGroupWiseLink, gwPAGERStopTrap=gwPAGERStopTrap, gwPAGERFgnLinkTrap=gwPAGERFgnLinkTrap, gateways=gateways, gwPAGERInStatuses=gwPAGERInStatuses, gwPAGEROutStatuses=gwPAGEROutStatuses)
