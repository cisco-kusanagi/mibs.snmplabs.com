#
# PySNMP MIB module EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Gauge32, MibIdentifier, Bits, NotificationType, Counter32, Integer32, Unsigned32, Counter64, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "MibIdentifier", "Bits", "NotificationType", "Counter32", "Integer32", "Unsigned32", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathOutboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19))
fastPathOutboundTelnetPrivate.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setOrganization('Broadcom Inc')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB", agentOutboundTelnetGroup=agentOutboundTelnetGroup, fastPathOutboundTelnetPrivate=fastPathOutboundTelnetPrivate, agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode, PYSNMP_MODULE_ID=fastPathOutboundTelnetPrivate, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions)
