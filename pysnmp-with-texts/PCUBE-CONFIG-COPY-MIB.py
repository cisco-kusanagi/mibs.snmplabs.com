#
# PySNMP MIB module PCUBE-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCUBE-CONFIG-COPY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
pcubeMgmt, = mibBuilder.importSymbols("PCUBE-SMI", "pcubeMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, NotificationType, Unsigned32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Bits, Counter64, ObjectIdentity, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Unsigned32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Bits", "Counter64", "ObjectIdentity", "iso", "Integer32", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pcubeConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 3, 1))
pcubeConfigCopyMIB.setRevisions(('2006-04-06 20:00', '2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcubeConfigCopyMIB.setRevisionsDescriptions(('The original mib has been chagned to use SMIv2 syntax. Clarified descriptions in the mib.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setLastUpdated('200604062000Z')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setDescription("This MIB facilitates writing of running configuration of the SCOS to startup configuration. A config-copy operation is a request to copy a configuration file of a running SCOS. The term 'agent-config' will be used in this MIB to refer to either the running config or the startup config. The term SCE refers to Service Control Engine")
class ConfigFileType(TextualConvention, Integer32):
    description = 'The various types of files on which a config-copy operation can be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("startupConfig", 1), ("runningConfig", 2))

pcubeConfigCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1))
pcubeConfigCopyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2))
pcubeConfigCopyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1))
pcubeConfigCopyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2))
pcubeCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1))
pcubeCopyTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1), )
if mibBuilder.loadTexts: pcubeCopyTable.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyTable.setDescription('A table of config-copy requests.')
pcubeCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1), ).setIndexNames((0, "PCUBE-CONFIG-COPY-MIB", "pcubeCopyIndex"))
if mibBuilder.loadTexts: pcubeCopyEntry.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyEntry.setDescription("A config-copy request. A management station wishing to save the running config may use any number to be used as an index. The station should then create the associated instance of the row status and row index objects. It should be noted however that currently 'pcubeCopySourceFileType' must be of 'runningConfig' type and 'pcubeCopyDestFileType' must be of 'startupConfig' type (that are the default values). After setting pcubeCopySourceFileType and pcubeCopyDestFileType objects by explicit SNMP request or or by default, the row status should be set to createAndGo to initiate the request. Note that this entire procedure may be initiated via a single set request which specifies a row status of 'createAndGo(4)'.")
pcubeCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pcubeCopyIndex.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyIndex.setDescription("Object which specifies a unique entry in the pcubeCopyTable. A management station wishing to initiate a config-copy operation should use a random value for this object when creating or modifying an instance of a 'pcubeCopyEntry'. The RowStatus semantics of the 'pcubeCopyEntryRowStatus' object will prevent access conflicts.")
pcubeCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyEntryRowStatus.setDescription('This object can be used for creating/deleting entries from the table.')
pcubeCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopySourceFileType.setStatus('current')
if mibBuilder.loadTexts: pcubeCopySourceFileType.setDescription("Specifies the type of file to copy from. Currently only 'runningConfig(2)' is supported.")
pcubeCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyDestFileType.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyDestFileType.setDescription("Specifies the type of file to copy to. currently only 'startupConfig(1)' is supported.")
pcubeConfigCopyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeConfigCopyMIBCompliance = pcubeConfigCopyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pcubeConfigCopyMIBCompliance.setDescription('A compliance statement defined in this MIB module, for SCE SNMP agents.')
pcubeCopyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyEntryRowStatus"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopySourceFileType"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopyDestFileType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeCopyGroup = pcubeCopyGroup.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyGroup.setDescription('A collection of objects used for specifying the configuration of the copy operation.')
mibBuilder.exportSymbols("PCUBE-CONFIG-COPY-MIB", pcubeCopy=pcubeCopy, pcubeConfigCopyMIBGroups=pcubeConfigCopyMIBGroups, pcubeCopyEntryRowStatus=pcubeCopyEntryRowStatus, pcubeCopyDestFileType=pcubeCopyDestFileType, pcubeConfigCopyMIBObjects=pcubeConfigCopyMIBObjects, pcubeConfigCopyMIBCompliances=pcubeConfigCopyMIBCompliances, pcubeCopyTable=pcubeCopyTable, pcubeCopyGroup=pcubeCopyGroup, pcubeCopyEntry=pcubeCopyEntry, ConfigFileType=ConfigFileType, PYSNMP_MODULE_ID=pcubeConfigCopyMIB, pcubeConfigCopyMIB=pcubeConfigCopyMIB, pcubeCopySourceFileType=pcubeCopySourceFileType, pcubeConfigCopyMIBConformance=pcubeConfigCopyMIBConformance, pcubeConfigCopyMIBCompliance=pcubeConfigCopyMIBCompliance, pcubeCopyIndex=pcubeCopyIndex)
