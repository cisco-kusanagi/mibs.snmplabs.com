#
# PySNMP MIB module VMWARE-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, ObjectIdentity, Integer32, Counter64, NotificationType, Gauge32, ModuleIdentity, Counter32, Bits, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "Counter32", "Bits", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 1))
vmwAgentCapabilityMIB.setRevisions(('2012-07-13 00:00', '2010-10-18 00:00', '2008-10-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for VMware ESX 5.1 agent added.', 'Capabilities for VMware ESX 5.0 added.', 'Capabilities for VMware ESX 4.0 added.',))
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setContactInfo('VMware, Inc 3401 Hillview Ave Palo Alto, CA 94304 Tel: 1-877-486-9273 or 650-427-5000 Fax: 650-427-5001 Web: http://communities.vmware.com/community/developer/forums/managementapi ')
if mibBuilder.loadTexts: vmwAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware agents by release. ')
vmwEsxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1))
vmwESX51x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setProductRelease('5.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX51x = vmwESX51x.setStatus('current')
if mibBuilder.loadTexts: vmwESX51x.setDescription('Release 5.1.x for VMware ESXi supports SNMPv1, SNMPv2c, and SNMPv3 with a stand-alone snmpd process. This agent supports read-only protocol operations. This implies that configuring the SNMPv3 Agent can not be done via SET operations. Hence IETF standard SNMPv3 agent configuration mibs are not provided. SNMPv3 protocol is fully supported once configured via the CLI command interface (esxcli system snmp) command set or host profiles. Lastly this SNMP agent provides one read-only view of the entire system to which all SNMPv3 users configured are assigned. ')
vmwESX51x.setReference('http://www.vmware.com/products')
vmwESX50x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setProductRelease('5.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX50x = vmwESX50x.setStatus('current')
if mibBuilder.loadTexts: vmwESX50x.setDescription('Release 5.0.x for VMware ESXi. The SNMPv1/v2c agent is a subsystem in the hostd process')
vmwESX50x.setReference('http://www.vmware.com/products')
vmwESX41x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setProductRelease('4.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX41x = vmwESX41x.setStatus('current')
if mibBuilder.loadTexts: vmwESX41x.setDescription('Release 4.1.x for VMware ESX, the SNMP agent is now a subsystem in the hostd process on ESXi.')
vmwESX41x.setReference('http://www.vmware.com/products')
vmwESX40x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setProductRelease('4.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwESX40x = vmwESX40x.setStatus('current')
if mibBuilder.loadTexts: vmwESX40x.setDescription('Release 4.0.x for VMware ESX. The SNMP agent is now part of the hostd process')
vmwESX40x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-AGENTCAP-MIB", vmwESX41x=vmwESX41x, vmwESX40x=vmwESX40x, vmwESX51x=vmwESX51x, vmwEsxCapability=vmwEsxCapability, vmwESX50x=vmwESX50x, vmwAgentCapabilityMIB=vmwAgentCapabilityMIB, PYSNMP_MODULE_ID=vmwAgentCapabilityMIB)
