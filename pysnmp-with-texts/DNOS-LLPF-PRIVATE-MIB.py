#
# PySNMP MIB module DNOS-LLPF-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-LLPF-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, IpAddress, NotificationType, TimeTicks, Integer32, ObjectIdentity, ModuleIdentity, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "IpAddress", "NotificationType", "TimeTicks", "Integer32", "ObjectIdentity", "ModuleIdentity", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
fastPathLlpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48))
fastPathLlpf.setRevisions(('2011-01-26 00:00', '2009-10-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathLlpf.setRevisionsDescriptions(('Postal address updated.', 'Dell branding related changes.',))
if mibBuilder.loadTexts: fastPathLlpf.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLlpf.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathLlpf.setContactInfo('')
if mibBuilder.loadTexts: fastPathLlpf.setDescription('The Broadcom Private MIB for DNOS Link Local Protocol Filtering.')
agentSwitchLlpfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1))
agentSwitchLlpfPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1), )
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigTable.setDescription('A table that contains the configuration objects for the with each port.')
agentSwitchLlpfPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DNOS-LLPF-PRIVATE-MIB", "agentSwitchLlpfProtocolType"))
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentSwitchLlpfPortConfigEntry.setDescription('The configuration information for LLPF.')
agentSwitchLlpfProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 6)))
if mibBuilder.loadTexts: agentSwitchLlpfProtocolType.setStatus('current')
if mibBuilder.loadTexts: agentSwitchLlpfProtocolType.setDescription("Port's LLPF protocol Type. It can be one of the following values isdp,vtp,dtp,udld,pagp,sstp,all.")
agentSwitchLlpfPortBlockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSwitchLlpfPortBlockMode.setStatus('current')
if mibBuilder.loadTexts: agentSwitchLlpfPortBlockMode.setDescription("Port's LLPF mode. It can be either enabled or disabled default will be disable.")
mibBuilder.exportSymbols("DNOS-LLPF-PRIVATE-MIB", agentSwitchLlpfProtocolType=agentSwitchLlpfProtocolType, fastPathLlpf=fastPathLlpf, agentSwitchLlpfPortConfigTable=agentSwitchLlpfPortConfigTable, agentSwitchLlpfGroup=agentSwitchLlpfGroup, PYSNMP_MODULE_ID=fastPathLlpf, agentSwitchLlpfPortConfigEntry=agentSwitchLlpfPortConfigEntry, agentSwitchLlpfPortBlockMode=agentSwitchLlpfPortBlockMode)
