#
# PySNMP MIB module BROCADE-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
brcdSysLog, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "brcdSysLog")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Unsigned32, IpAddress, MibIdentifier, NotificationType, Counter64, Counter32, Gauge32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Counter64", "Counter32", "Gauge32", "iso", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
brocadeSysLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1))
brocadeSysLogMIB.setRevisions(('2011-11-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: brocadeSysLogMIB.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: brocadeSysLogMIB.setLastUpdated('201111040000Z')
if mibBuilder.loadTexts: brocadeSysLogMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: brocadeSysLogMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: brocadeSysLogMIB.setDescription("This MIB module contains the managed object definitions for syslog Copyright 1996-2011 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
brcdSysLogGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1))
brcdSysLogServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1), )
if mibBuilder.loadTexts: brcdSysLogServerTable.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerTable.setDescription('System Log Server table.')
brcdSysLogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1), ).setIndexNames((0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddrType"), (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddr"), (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerUDPPort"))
if mibBuilder.loadTexts: brcdSysLogServerEntry.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerEntry.setDescription('A row in the System Log Server table.')
brcdSysLogServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: brcdSysLogServerAddrType.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerAddrType.setDescription('The syslog server address type. The supported address types are ipv4(1) and ipv6(2).')
brcdSysLogServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: brcdSysLogServerAddr.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerAddr.setDescription('IP address of syslog server.')
brcdSysLogServerUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: brcdSysLogServerUDPPort.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerUDPPort.setDescription('UDP port number of syslog server.')
brcdSysLogServerOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brcdSysLogServerOutPkts.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerOutPkts.setDescription('Number of sylog packets sent to this syslog server.')
brcdSysLogServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: brcdSysLogServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: brcdSysLogServerRowStatus.setDescription('Setting this object to createAndGo(4) results in addition of new row. Setting this object to destroy( 6)results in removal of a row. The value active(1) is returned for get and get-next requests. Other values in the enumeration are not used.')
mibBuilder.exportSymbols("BROCADE-SYSLOG-MIB", PYSNMP_MODULE_ID=brocadeSysLogMIB, brocadeSysLogMIB=brocadeSysLogMIB, brcdSysLogGroup=brcdSysLogGroup, brcdSysLogServerTable=brcdSysLogServerTable, brcdSysLogServerAddr=brcdSysLogServerAddr, brcdSysLogServerRowStatus=brcdSysLogServerRowStatus, brcdSysLogServerAddrType=brcdSysLogServerAddrType, brcdSysLogServerEntry=brcdSysLogServerEntry, brcdSysLogServerUDPPort=brcdSysLogServerUDPPort, brcdSysLogServerOutPkts=brcdSysLogServerOutPkts)
