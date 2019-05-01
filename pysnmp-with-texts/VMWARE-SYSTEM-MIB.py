#
# PySNMP MIB module VMWARE-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibIdentifier, iso, Counter64, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, ObjectIdentity, Integer32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "iso", "Counter64", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 10))
vmwSystemMIB.setRevisions(('2010-08-02 00:00', '2008-01-12 00:00', '2007-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwSystemMIB.setRevisionsDescriptions(('Add vmwProdPatch managed object to report patch level', 'Add to comments the Managed Object Browser (MOB) URLs which provide data this MIB module exposes.', 'This is the first revision in SMIv2 format. One object (vmwProdOID) has been dropped from the original SMIv1 version as it duplicates sysObjectId from SNMPv2-MIB.',))
if mibBuilder.loadTexts: vmwSystemMIB.setLastUpdated('201008020000Z')
if mibBuilder.loadTexts: vmwSystemMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwSystemMIB.setContactInfo('VMware, Inc 3401 Hillview Ave Palo Alto, CA 94304 Tel: 1-877-486-9273 or 650-427-5000 Fax: 650-427-5001 Web: http://communities.vmware.com/community/developer/forums/managementapi ')
if mibBuilder.loadTexts: vmwSystemMIB.setDescription('This MIB module provides for System Software identification')
vmwProdName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdName.setStatus('current')
if mibBuilder.loadTexts: vmwProdName.setDescription("This product's name. VIM Property: AboutInfo.name https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout")
vmwProdVersion = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdVersion.setStatus('current')
if mibBuilder.loadTexts: vmwProdVersion.setDescription("The product's version release identifier. Format is Major.Minor.Update VIM Property: AboutInfo.version https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout")
vmwProdBuild = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdBuild.setStatus('current')
if mibBuilder.loadTexts: vmwProdBuild.setDescription('This identifier represents the most specific identifier. VIM Property: AboutInfo.build https://esx.example.com/mob/?moid=ServiceInstance&doPath=content%2eabout')
vmwProdUpdate = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdUpdate.setStatus('current')
if mibBuilder.loadTexts: vmwProdUpdate.setDescription('This identifier represents the update level applied to this system. VIM Property: Advanced Options key: Misc.HostAgentUpdateLevel https://esx.example.com/mob/?moid=ha%2dadv%2doptions')
vmwProdPatch = MibScalar((1, 3, 6, 1, 4, 1, 6876, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmwProdPatch.setStatus('current')
if mibBuilder.loadTexts: vmwProdPatch.setDescription('This identifier represents the patch level applied to this system. VIM Property: None. CLI: esxcli system version get')
vmwSystemMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2))
vmwSystemMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1))
vmwSysMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2))
vmwSysMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 1, 2)).setObjects(("VMWARE-SYSTEM-MIB", "vmwSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSysMIBBasicCompliance = vmwSysMIBBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: vmwSysMIBBasicCompliance.setDescription('The compliance statement for entities which implement the VMWARE-SYSTEM-MIB.')
vmwSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 1, 10, 2, 2, 1)).setObjects(("VMWARE-SYSTEM-MIB", "vmwProdName"), ("VMWARE-SYSTEM-MIB", "vmwProdVersion"), ("VMWARE-SYSTEM-MIB", "vmwProdBuild"), ("VMWARE-SYSTEM-MIB", "vmwProdUpdate"), ("VMWARE-SYSTEM-MIB", "vmwProdPatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwSystemGroup = vmwSystemGroup.setStatus('current')
if mibBuilder.loadTexts: vmwSystemGroup.setDescription('These objects uniquely identifies a given VMware system software image.')
mibBuilder.exportSymbols("VMWARE-SYSTEM-MIB", vmwSystemMIBCompliances=vmwSystemMIBCompliances, vmwSysMIBGroups=vmwSysMIBGroups, vmwSystemMIBConformance=vmwSystemMIBConformance, vmwProdName=vmwProdName, vmwProdBuild=vmwProdBuild, vmwProdUpdate=vmwProdUpdate, vmwSystemGroup=vmwSystemGroup, vmwProdVersion=vmwProdVersion, PYSNMP_MODULE_ID=vmwSystemMIB, vmwProdPatch=vmwProdPatch, vmwSystemMIB=vmwSystemMIB, vmwSysMIBBasicCompliance=vmwSysMIBBasicCompliance)
