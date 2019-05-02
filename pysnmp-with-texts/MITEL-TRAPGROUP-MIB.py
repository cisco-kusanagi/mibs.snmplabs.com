#
# PySNMP MIB module MITEL-TRAPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-TRAPGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, ObjectIdentity, Unsigned32, IpAddress, TimeTicks, Counter64, ModuleIdentity, MibIdentifier, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks", "Counter64", "ModuleIdentity", "MibIdentifier", "Counter32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelRouterSnmpTrapGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mitelRouterSnmpTrapGroup.setRevisions(('2003-03-24 10:50', '2002-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setRevisionsDescriptions(('Convert to SMIv2', 'Mitel IP Networking Trap MIB version 1.0',))
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setLastUpdated('200303241050Z')
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelRouterSnmpTrapGroup.setDescription('The Mitel IP Networking Trap MIB.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelSnmpTrapGlobal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapGlobal.setStatus('current')
if mibBuilder.loadTexts: mitelSnmpTrapGlobal.setDescription('Enable/disable all traps sending traps to remote locations.')
mitelSnmpTrapControl = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelSnmpTrapControl.setStatus('current')
if mibBuilder.loadTexts: mitelSnmpTrapControl.setDescription('A bit string used to represent the enable/disable state of all traps in in the system. The bit positions are: 1 Cold Start 2 Link Down 4 Link Up 8 Authentication Failure 16 New Root (Rfc 1493) 32 Topology Change (Rfc 1493) 64 Mitel IP Access Restriction 128 Mitel Retry Threshold Reached 256 Mitel DHCP Client Obtained IP 512 Mitel DHCP Client Lease Expired 1024 Mitel Call Control Failed to Seize Line 2048 Mitel Call Control DDI Mapping Error 4096 Mitel Voice Mail Disk Nearly Full 8192 Mitel Voice Mail Disk Full 16384 DSX1 Line Status 32768 Mitel Application Monitor Task Crashed')
mibBuilder.exportSymbols("MITEL-TRAPGROUP-MIB", mitelPropIpNetworking=mitelPropIpNetworking, mitelProprietary=mitelProprietary, mitelIpNetRouter=mitelIpNetRouter, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, mitel=mitel, mitelSnmpTrapControl=mitelSnmpTrapControl, mitelSnmpTrapGlobal=mitelSnmpTrapGlobal, PYSNMP_MODULE_ID=mitelRouterSnmpTrapGroup)
