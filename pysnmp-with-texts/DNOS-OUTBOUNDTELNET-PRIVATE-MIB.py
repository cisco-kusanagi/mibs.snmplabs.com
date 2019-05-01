#
# PySNMP MIB module DNOS-OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, MibIdentifier, Counter64, Gauge32, Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, iso, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "iso", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathOutboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19))
fastPathOutboundTelnetPrivate.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setRevisionsDescriptions(('Add new Postal address change.', 'Dell branding related changes.',))
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setContactInfo('')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setDescription('The Broadcom Private MIB for DNOS Outbound Telnet')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setDescription(' Admin-mode of the Outbound Telnet.')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setDescription(' The maximum no. of Outbound Telnet sessions allowed.')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setDescription('The login inactivity timeout value for Outbound Telnet.')
mibBuilder.exportSymbols("DNOS-OUTBOUNDTELNET-PRIVATE-MIB", agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, fastPathOutboundTelnetPrivate=fastPathOutboundTelnetPrivate, agentOutboundTelnetGroup=agentOutboundTelnetGroup, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode, PYSNMP_MODULE_ID=fastPathOutboundTelnetPrivate)
