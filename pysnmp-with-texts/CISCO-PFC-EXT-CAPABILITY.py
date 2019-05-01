#
# PySNMP MIB module CISCO-PFC-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PFC-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Gauge32, Counter64, NotificationType, Bits, ModuleIdentity, iso, MibIdentifier, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Gauge32", "Counter64", "NotificationType", "Bits", "ModuleIdentity", "iso", "MibIdentifier", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPfcExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 626))
ciscoPfcExtCapability.setRevisions(('2014-08-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPfcExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPfcExtCapability.setLastUpdated('201408110000Z')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setDescription('The capabilities description of CISCO-PFC-EXT-MIB.')
cpeCapNxOSV06R0002U0201PN3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 626, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus \n                        3000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setStatus('current')
if mibBuilder.loadTexts: cpeCapNxOSV06R0002U0201PN3k.setDescription('CISCO-PFC-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-PFC-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPfcExtCapability, ciscoPfcExtCapability=ciscoPfcExtCapability, cpeCapNxOSV06R0002U0201PN3k=cpeCapNxOSV06R0002U0201PN3k)
