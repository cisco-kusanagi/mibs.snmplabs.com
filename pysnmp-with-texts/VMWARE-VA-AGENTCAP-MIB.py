#
# PySNMP MIB module VMWARE-VA-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-VA-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, MibIdentifier, TimeTicks, iso, ObjectIdentity, IpAddress, Counter32, NotificationType, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "IpAddress", "Counter32", "NotificationType", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVAAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 5))
vmwVAAgentCapabilityMIB.setRevisions(('2015-01-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for VMware Virutal Appliance.',))
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setLastUpdated('201501120000Z')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setContactInfo('VMware, Inc 3401 Hillview Ave Palo Alto, CA 94304 Tel: 1-877-486-9273 or 650-427-5000 Fax: 650-427-5001 Web: http://communities.vmware.com/community/developer/forums/managementapi ')
if mibBuilder.loadTexts: vmwVAAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware Virtual Appliance agents by release.')
vmwVACapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1))
vmwVA2015x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setProductRelease('6.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVA2015x = vmwVA2015x.setStatus('current')
if mibBuilder.loadTexts: vmwVA2015x.setDescription("Release 2015 aka 6.0 for VMware Virtual Appliance supporting SNMPv1, SNMPv2c, and SNMPv3. This agent supports read-only protocol operations, shares same configuration file as VMware ESXi agent. This implies that configuring the SNMPv3 Agent can not be done via SET operations or use SET PDU to discover engine id. Hence IETF standard SNMPv3 agent configuration mibs are not provided. The SNMPv3 protocol is fully supported once configured via the CLI command interface, run applianceh shell using the 'snmp' command set. Lastly this SNMP agent provides one read-only view of the entire system to which all SNMPv3 users configured are assigned. This initial release does not have: UDP-MIB, TCP-MIB modules. ")
vmwVA2015x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-VA-AGENTCAP-MIB", vmwVA2015x=vmwVA2015x, vmwVAAgentCapabilityMIB=vmwVAAgentCapabilityMIB, PYSNMP_MODULE_ID=vmwVAAgentCapabilityMIB, vmwVACapability=vmwVACapability)
