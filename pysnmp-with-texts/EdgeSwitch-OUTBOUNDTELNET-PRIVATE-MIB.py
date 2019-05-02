#
# PySNMP MIB module EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ObjectIdentity, MibIdentifier, Unsigned32, Gauge32, Bits, TimeTicks, ModuleIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Gauge32", "Bits", "TimeTicks", "ModuleIdentity", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathOutboundTelnetPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19))
fastPathOutboundTelnetPrivate.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setRevisionsDescriptions(('Add new Postal address change.', 'Ubiquiti branding related changes.',))
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setContactInfo('')
if mibBuilder.loadTexts: fastPathOutboundTelnetPrivate.setDescription('The Ubiquiti Private MIB for EdgeSwitch Outbound Telnet')
agentOutboundTelnetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1))
agentOutboundTelnetAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetAdminMode.setDescription(' Admin-mode of the Outbound Telnet.')
agentOutboundTelnetMaxNoOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetMaxNoOfSessions.setDescription(' The maximum no. of Outbound Telnet sessions allowed.')
agentOutboundTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setStatus('current')
if mibBuilder.loadTexts: agentOutboundTelnetTimeout.setDescription(' The login inactivity timeout value for Outbound Telnet.')
mibBuilder.exportSymbols("EdgeSwitch-OUTBOUNDTELNET-PRIVATE-MIB", agentOutboundTelnetTimeout=agentOutboundTelnetTimeout, fastPathOutboundTelnetPrivate=fastPathOutboundTelnetPrivate, agentOutboundTelnetGroup=agentOutboundTelnetGroup, PYSNMP_MODULE_ID=fastPathOutboundTelnetPrivate, agentOutboundTelnetMaxNoOfSessions=agentOutboundTelnetMaxNoOfSessions, agentOutboundTelnetAdminMode=agentOutboundTelnetAdminMode)
