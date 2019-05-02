#
# PySNMP MIB module VMWARE-NSX-MANAGER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, IpAddress, Counter32, MibIdentifier, ModuleIdentity, TimeTicks, Gauge32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "IpAddress", "Counter32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwNSXAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 25))
vmwNSXAgentCapabilityMIB.setRevisions(('2016-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setRevisionsDescriptions(('Capabilities for NSX Manager releases.',))
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setLastUpdated('201606020000Z')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setContactInfo('VMware, Inc 3401 Hillview Ave Palo Alto, CA 94304 Tel: 1-877-486-9273 or 650-427-5000 Fax: 650-427-5001 Web: http://communities.vmware.com/community/developer/forums/managementapi ')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setDescription('This module defines agent capabilities for deployed VMware NSX Manager agents by release.')
vmwNSXMCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1))
vmwNSXManager2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setProductRelease('6.5.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setStatus('current')
if mibBuilder.loadTexts: vmwNSXManager2016x.setDescription('Release 6.5 for VMware NSX Manager supporting only SNMPv2c trap PDUs. It describes all the notifications sent from the NSX Manager appliance. WARNING: This mib module will not be backward compatible with next version. ')
vmwNSXManager2016x.setReference('http://www.vmware.com/products')
mibBuilder.exportSymbols("VMWARE-NSX-MANAGER-AGENTCAP-MIB", vmwNSXMCapability=vmwNSXMCapability, vmwNSXAgentCapabilityMIB=vmwNSXAgentCapabilityMIB, vmwNSXManager2016x=vmwNSXManager2016x, PYSNMP_MODULE_ID=vmwNSXAgentCapabilityMIB)
