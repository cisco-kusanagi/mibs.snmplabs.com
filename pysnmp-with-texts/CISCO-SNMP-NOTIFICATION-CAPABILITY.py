#
# PySNMP MIB module CISCO-SNMP-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-NOTIFICATION-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, Counter64, TimeTicks, Unsigned32, Gauge32, ModuleIdentity, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, IpAddress, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "TimeTicks", "Unsigned32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "IpAddress", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 330))
ciscoSnmpNotificationCapability.setRevisions(('2008-06-25 00:00', '2006-03-29 00:00', '2004-07-28 00:00', '2003-08-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setRevisionsDescriptions(('Added capability statement cSnmpNotifCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cSnmpNotifCapACSWV03R000 for Application Control Engine (ACE).', 'Added capability for VISM Release 3.3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setLastUpdated('200806250000Z')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpNotificationCapability.setDescription('The capabilities description of SNMP-NOTIFICATION-MIB.')
cSnmpNotifCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapCatOSV05R0501 = cSnmpNotifCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: cSnmpNotifCapCatOSV05R0501.setDescription('SNMP-NOTIFICATION-MIB capabilities.')
cSnmpNotifCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapVISM33 = cSnmpNotifCapVISM33.setStatus('current')
if mibBuilder.loadTexts: cSnmpNotifCapVISM33.setDescription('SNMP-NOTIFICATION-MIB capabilities.')
cSnmpNotifCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapACSWV03R000 = cSnmpNotifCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpNotifCapACSWV03R000.setDescription('SNMP-NOTIFICATION-MIB capabilities.')
cSnmpNotifCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 330, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpNotifCapc4710aceVA1R700 = cSnmpNotifCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpNotifCapc4710aceVA1R700.setDescription('SNMP-NOTIFICATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-NOTIFICATION-CAPABILITY", cSnmpNotifCapCatOSV05R0501=cSnmpNotifCapCatOSV05R0501, cSnmpNotifCapACSWV03R000=cSnmpNotifCapACSWV03R000, PYSNMP_MODULE_ID=ciscoSnmpNotificationCapability, cSnmpNotifCapc4710aceVA1R700=cSnmpNotifCapc4710aceVA1R700, ciscoSnmpNotificationCapability=ciscoSnmpNotificationCapability, cSnmpNotifCapVISM33=cSnmpNotifCapVISM33)
