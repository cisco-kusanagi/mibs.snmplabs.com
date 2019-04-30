#
# PySNMP MIB module CISCO-PFC-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PFC-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Integer32, Bits, Unsigned32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, IpAddress, Counter64, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "IpAddress", "Counter64", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPfcExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 626))
ciscoPfcExtCapability.setRevisions(('2014-08-11 00:00',))
if mibBuilder.loadTexts: ciscoPfcExtCapability.setLastUpdated('201408110000Z')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setOrganization('Cisco Systems, Inc.')
cpeCapNxOSV06R0002U0201PN3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 626, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus \n                        3000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setStatus('current')
mibBuilder.exportSymbols("CISCO-PFC-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPfcExtCapability, ciscoPfcExtCapability=ciscoPfcExtCapability, cpeCapNxOSV06R0002U0201PN3k=cpeCapNxOSV06R0002U0201PN3k)
