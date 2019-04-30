#
# PySNMP MIB module CISCO-PSM-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PSM-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Gauge32, ObjectIdentity, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier, Bits, Integer32, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier", "Bits", "Integer32", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPsmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoPsmMibCapability.setRevisions(('2003-08-05 00:00',))
if mibBuilder.loadTexts: ciscoPsmMibCapability.setLastUpdated('200308050000Z')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setOrganization('Cisco Systems, Inc.')
ciscoPsmMibCapabilityMDS12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setProductRelease('Cisco MDS 1.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-PSM-MIB-CAPABILITY", ciscoPsmMibCapability=ciscoPsmMibCapability, PYSNMP_MODULE_ID=ciscoPsmMibCapability, ciscoPsmMibCapabilityMDS12R0=ciscoPsmMibCapabilityMDS12R0)
