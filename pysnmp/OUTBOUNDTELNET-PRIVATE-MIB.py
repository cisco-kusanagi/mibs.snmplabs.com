#
# PySNMP MIB module OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, IpAddress, Counter32, iso, Integer32, TimeTicks, ModuleIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "IpAddress", "Counter32", "iso", "Integer32", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
outboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 19))
if mibBuilder.loadTexts: outboundTelnetPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: outboundTelnetPrivate.setOrganization('QCI')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
mibBuilder.exportSymbols("OUTBOUNDTELNET-PRIVATE-MIB", PYSNMP_MODULE_ID=outboundTelnetPrivate, agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, agentOutboundTelnetGroup=agentOutboundTelnetGroup, outboundTelnetPrivate=outboundTelnetPrivate, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode)
