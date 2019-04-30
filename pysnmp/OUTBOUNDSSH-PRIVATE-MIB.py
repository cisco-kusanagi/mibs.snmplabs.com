#
# PySNMP MIB module OUTBOUNDSSH-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OUTBOUNDSSH-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, iso, Integer32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, NotificationType, MibIdentifier, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "iso", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
outboundSSHPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 21))
if mibBuilder.loadTexts: outboundSSHPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: outboundSSHPrivate.setOrganization('QCI')
agentOutboundSSHGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1))
agentOutboundSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHAdminMode.setStatus('current')
agentOutboundSSHMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHMaxNoOfSessions.setStatus('current')
agentOutboundSSHTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundSSHTimeout.setStatus('current')
mibBuilder.exportSymbols("OUTBOUNDSSH-PRIVATE-MIB", PYSNMP_MODULE_ID=outboundSSHPrivate, agentOutboundSSHTimeout=agentOutboundSSHTimeout, agentOutboundSSHMaxNoOfSessions=agentOutboundSSHMaxNoOfSessions, agentOutboundSSHGroup=agentOutboundSSHGroup, agentOutboundSSHAdminMode=agentOutboundSSHAdminMode, outboundSSHPrivate=outboundSSHPrivate)
