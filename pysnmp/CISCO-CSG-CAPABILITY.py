#
# PySNMP MIB module CISCO-CSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CSG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Counter64, Counter32, Integer32, IpAddress, Unsigned32, NotificationType, Bits, Gauge32, MibIdentifier, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter64", "Counter32", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "Bits", "Gauge32", "MibIdentifier", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCsgCapability.setRevisions(('2003-05-01 00:00',))
if mibBuilder.loadTexts: ciscoCsgCapability.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: ciscoCsgCapability.setOrganization('Cisco Systems, Inc.')
ciscoCsgCapabilityV14R02ZA1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setProductRelease('Cisco IOS 12.2(14)ZA1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CSG-CAPABILITY", PYSNMP_MODULE_ID=ciscoCsgCapability, ciscoCsgCapabilityV14R02ZA1=ciscoCsgCapabilityV14R02ZA1, ciscoCsgCapability=ciscoCsgCapability)
