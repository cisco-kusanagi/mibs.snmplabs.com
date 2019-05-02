#
# PySNMP MIB module CLAB-TOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CLAB-TOPO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, ObjectIdentity, ModuleIdentity, Bits, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Bits", "iso", "TimeTicks", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
clabTopoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 2))
clabTopoMib.setRevisions(('2017-06-15 00:00', '2009-01-21 00:00', '2006-12-07 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: clabTopoMib.setRevisionsDescriptions(('Revised Version includes ECN CLAB-TOPO-MIB-N-17.0161-1 to add Apache License.', 'Revised Version includes ECNs OSSIv3.0-N-08.0651-3 OSSIv3.0-N-08.0700-4 and published as I08', 'Initial version, published as part of the CableLabs OSSIv3.0 specification CM-SP-OSSIv3.0-I01-061207 Copyright 1999-2009 Cable Television Laboratories, Inc. All rights reserved.',))
if mibBuilder.loadTexts: clabTopoMib.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: clabTopoMib.setOrganization('Cable Television Laboratories, Inc.')
if mibBuilder.loadTexts: clabTopoMib.setContactInfo(' Postal: Cable Television Laboratories, Inc. 858 Coal Creek Circle Louisville, Colorado 80027-9750 U.S.A. Phone: +1 303-661-9100 Fax: +1 303-661-9199 E-mail: mibs@cablelabs.com')
if mibBuilder.loadTexts: clabTopoMib.setDescription("Licensed under the Apache License, Version 2.0 (the 'License'); you may not use this file except in compliance with the License. You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. This MIB module contains the management objects for the management of fiber nodes in the Cable plant. Copyright 2006-2017 Cable Television Laboratories, Inc. All rights reserved.")
class NodeName(TextualConvention, OctetString):
    reference = 'RFC 3411.'
    description = 'This data type is a human readable string that represents the name of a fiber node. Internationalization is supported by conforming to the SNMP textual convention SnmpAdminString. The US-ASCII control characters (0x00 0x1F), the DEL Character (0x7F), and the double-quote mark (0x22) are prohibited within the syntax of this data type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

clabTopoMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1))
clabTopoFiberNodeCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1), )
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setDescription('This object defines the cable HFC plant Fiber Nodes known at a CMTS. This object supports the creation and deletion of multiple instances.')
clabTopoFiberNodeCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setDescription('The conceptual row of clabTopoFiberNodeCfg. The CMTS persists all instances of FiberNodeCfg across reinitializations.')
clabTopoFiberNodeCfgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 1), NodeName().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setReference('DOCSIS 3.0 MAC and Upper Layer Protocols Interface Specification CM-SP-MULPIv3.0-I01-060804, RF Topology Configuration section.')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setDescription('This key represents a human-readable name for a fiber node.')
clabTopoFiberNodeCfgNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 2), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setDescription('Administratively configured human-readable description of the fiber node')
clabTopoFiberNodeCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setDescription('The status of this instance.')
clabTopoChFnCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2), )
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setDescription("This object defines the RF topology by defining the connectivity of a CMTS's downstream and upstream channels to the fiber nodes. Each instance of this object describes connectivity of one downstream or upstream channel with a single fiber node. This object supports the creation and deletion of multiple instances.")
clabTopoChFnCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"), (0, "CLAB-TOPO-MIB", "clabTopoChFnCfgChIfIndex"))
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setDescription('The conceptual row of clabTopoChFnCfg. The CMTS persists all instances of ChFnCfg across reinitializations.')
clabTopoChFnCfgChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: clabTopoChFnCfgChIfIndex.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgChIfIndex.setDescription('This key represents the interface index of an upstream or downstream channel associated with this fiber node. In the upstream direction, only ifIndices docsCableUpstream channels are reflected.')
clabTopoChFnCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoChFnCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: clabTopoChFnCfgRowStatus.setDescription('The status of this instance.')
clabTopoMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2))
clabTopoMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1))
clabTopoMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2))
clabTopoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoCompliance = clabTopoCompliance.setStatus('current')
if mibBuilder.loadTexts: clabTopoCompliance.setDescription('The compliance statement for devices that implement the CableLabs Topology MIB.')
clabTopoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeDescr"), ("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgRowStatus"), ("CLAB-TOPO-MIB", "clabTopoChFnCfgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoGroup = clabTopoGroup.setStatus('current')
if mibBuilder.loadTexts: clabTopoGroup.setDescription('Group of objects implemented in the CMTS.')
mibBuilder.exportSymbols("CLAB-TOPO-MIB", clabTopoMibObjects=clabTopoMibObjects, clabTopoMibCompliances=clabTopoMibCompliances, clabTopoGroup=clabTopoGroup, PYSNMP_MODULE_ID=clabTopoMib, clabTopoFiberNodeCfgNodeName=clabTopoFiberNodeCfgNodeName, clabTopoMibConformance=clabTopoMibConformance, clabTopoFiberNodeCfgRowStatus=clabTopoFiberNodeCfgRowStatus, clabTopoCompliance=clabTopoCompliance, clabTopoFiberNodeCfgEntry=clabTopoFiberNodeCfgEntry, clabTopoMibGroups=clabTopoMibGroups, clabTopoChFnCfgChIfIndex=clabTopoChFnCfgChIfIndex, clabTopoChFnCfgEntry=clabTopoChFnCfgEntry, clabTopoFiberNodeCfgTable=clabTopoFiberNodeCfgTable, clabTopoChFnCfgTable=clabTopoChFnCfgTable, clabTopoChFnCfgRowStatus=clabTopoChFnCfgRowStatus, clabTopoMib=clabTopoMib, clabTopoFiberNodeCfgNodeDescr=clabTopoFiberNodeCfgNodeDescr, NodeName=NodeName)
