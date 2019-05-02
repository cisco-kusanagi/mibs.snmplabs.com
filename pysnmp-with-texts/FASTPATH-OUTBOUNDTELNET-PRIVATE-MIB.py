#
# PySNMP MIB module FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Integer32, ObjectIdentity, IpAddress, TimeTicks, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Integer32", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathOutboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19))
fastPathOutboundTelnetPrivate.setRevisions(('2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setRevisionsDescriptions(('Broadcom branding related changes.',))
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setContactInfo(' Customer Support Postal: Broadcom Corporation 13000 Weston Parkway Suite #105 Cary, NC 27513 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setDescription('The Broadcom Private MIB for FASTPATH Outbound Telnet')
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
mibBuilder.exportSymbols("FASTPATH-OUTBOUNDTELNET-PRIVATE-MIB", agentOutboundTelnetGroup=agentOutboundTelnetGroup, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, fastPathOutboundTelnetPrivate=fastPathOutboundTelnetPrivate, agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, PYSNMP_MODULE_ID=fastPathOutboundTelnetPrivate)
