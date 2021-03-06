#
# PySNMP MIB module MITEL-WANBACKUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-WANBACKUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, Integer32, Counter32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Gauge32, enterprises, Bits, MibIdentifier, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Integer32", "Counter32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Gauge32", "enterprises", "Bits", "MibIdentifier", "IpAddress", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
mitelIpGrpBackupWANGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6))
mitelIpGrpBackupWANGroup.setRevisions(('2003-03-24 11:03', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpBackupWANGroup.setRevisionsDescriptions(('IP MIB Version 1.0', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpBackupWANGroup.setLastUpdated('200303241103Z')
if mibBuilder.loadTexts: mitelIpGrpBackupWANGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpBackupWANGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpBackupWANGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelBackupWANDestIndex = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelBackupWANDestIndex.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANDestIndex.setDescription('Identifies the destination used to backup WAN Ethernet connection.')
mitelBackupWANEnable = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelBackupWANEnable.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANEnable.setDescription('Enables or disables the backup WAN Ethernet application.')
mitelBackupWANPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelBackupWANPollFreq.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANPollFreq.setDescription('This object tells the WAN Ethernet application how often it polls the destination. ')
mitelBackupWANLinkStatus = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelBackupWANLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANLinkStatus.setDescription('Shows whether the backup is up and running, or down. ')
mitelBackupWANServerTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5), )
if mibBuilder.loadTexts: mitelBackupWANServerTable.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerTable.setDescription('This table is a list of servers the Backup WAN application monitors.')
mitelBackupWANServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1), ).setIndexNames((0, "MITEL-WANBACKUP-MIB", "mitelBackupWANServerIPAddr"))
if mibBuilder.loadTexts: mitelBackupWANServerEntry.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerEntry.setDescription('Each entry in this table contains information of a server.')
mitelBackupWANServerIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelBackupWANServerIPAddr.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerIPAddr.setDescription('The IP address of the destination. It is used by the Backup WAN Ethernet application to send monitoring requests to. ')
mitelBackupWANServerSubnetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelBackupWANServerSubnetAddr.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerSubnetAddr.setDescription('The subnet address of the destination. ')
mitelBackupWANServerPrimary = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelBackupWANServerPrimary.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerPrimary.setDescription('Specifies whether this server is primary. ')
mitelBackupWANServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6, 5, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelBackupWANServerStatus.setStatus('current')
if mibBuilder.loadTexts: mitelBackupWANServerStatus.setDescription('The current status of this entry. ')
mibBuilder.exportSymbols("MITEL-WANBACKUP-MIB", mitelRouterIpGroup=mitelRouterIpGroup, mitelIpGrpBackupWANGroup=mitelIpGrpBackupWANGroup, mitelBackupWANServerEntry=mitelBackupWANServerEntry, mitelBackupWANDestIndex=mitelBackupWANDestIndex, mitelIpNetRouter=mitelIpNetRouter, mitelBackupWANPollFreq=mitelBackupWANPollFreq, mitelPropIpNetworking=mitelPropIpNetworking, mitelBackupWANServerPrimary=mitelBackupWANServerPrimary, mitel=mitel, PYSNMP_MODULE_ID=mitelIpGrpBackupWANGroup, mitelBackupWANServerIPAddr=mitelBackupWANServerIPAddr, mitelBackupWANServerStatus=mitelBackupWANServerStatus, mitelBackupWANEnable=mitelBackupWANEnable, mitelBackupWANServerSubnetAddr=mitelBackupWANServerSubnetAddr, mitelBackupWANServerTable=mitelBackupWANServerTable, mitelBackupWANLinkStatus=mitelBackupWANLinkStatus, mitelProprietary=mitelProprietary)
