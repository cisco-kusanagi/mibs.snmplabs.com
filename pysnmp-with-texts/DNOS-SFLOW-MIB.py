#
# PySNMP MIB module DNOS-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-SFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks, iso, ObjectIdentity, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks", "iso", "ObjectIdentity", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59))
if mibBuilder.loadTexts: fastPathSflow.setLastUpdated('201201120000Z')
if mibBuilder.loadTexts: fastPathSflow.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathSflow.setContactInfo('')
if mibBuilder.loadTexts: fastPathSflow.setDescription('The Dell Networking Private MIB for SFLOW')
agentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1))
agentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSflowSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentSflowSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates source-interface is un-configured.')
mibBuilder.exportSymbols("DNOS-SFLOW-MIB", agentFastPathSflowObjects=agentFastPathSflowObjects, agentSflowSourceInterface=agentSflowSourceInterface, fastPathSflow=fastPathSflow, PYSNMP_MODULE_ID=fastPathSflow)
