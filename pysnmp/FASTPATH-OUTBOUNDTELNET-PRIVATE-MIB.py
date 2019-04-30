#
# PySNMP MIB module FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:58:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits, Gauge32, iso, Unsigned32, NotificationType, Integer32, Counter32, IpAddress, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits", "Gauge32", "iso", "Unsigned32", "NotificationType", "Integer32", "Counter32", "IpAddress", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathOutboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19))
fastPathOutboundTelnetPrivate.setRevisions(('2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setOrganization('Broadcom Corporation')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB", agentOutboundTelnetGroup=agentOutboundTelnetGroup, PYSNMP_MODULE_ID=fastPathOutboundTelnetPrivate, agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, fastPathOutboundTelnetPrivate=fastPathOutboundTelnetPrivate)
