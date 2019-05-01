#
# PySNMP MIB module EdgeSwitch-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-SFLOW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Unsigned32, Integer32, ObjectIdentity, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, iso, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "iso", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59))
if mibBuilder.loadTexts: fastPathSflow.setLastUpdated('201201120000Z')
if mibBuilder.loadTexts: fastPathSflow.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathSflow.setContactInfo('')
if mibBuilder.loadTexts: fastPathSflow.setDescription('The Ubiquiti Private MIB for FastPath SFLOW')
agentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1))
agentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSflowSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentSflowSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates source-interface is un-configured.')
mibBuilder.exportSymbols("EdgeSwitch-SFLOW-MIB", PYSNMP_MODULE_ID=fastPathSflow, agentFastPathSflowObjects=agentFastPathSflowObjects, agentSflowSourceInterface=agentSflowSourceInterface, fastPathSflow=fastPathSflow)
