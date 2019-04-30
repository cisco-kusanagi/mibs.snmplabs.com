#
# PySNMP MIB module ASCEND-MIBIPSECPOLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPSECPOLICY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter64, MibIdentifier, IpAddress, Gauge32, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter64", "MibIdentifier", "IpAddress", "Gauge32", "ModuleIdentity", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibmibProfIpsecPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 167))
mibmibProfIpsecPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 167, 1), )
if mibBuilder.loadTexts: mibmibProfIpsecPolicyTable.setStatus('mandatory')
mibmibProfIpsecPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPSECPOLICY-MIB", "mibProfIpsecPolicy-PolicyName"))
if mibBuilder.loadTexts: mibmibProfIpsecPolicyEntry.setStatus('mandatory')
mibProfIpsecPolicy_PolicyName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 1), DisplayString()).setLabel("mibProfIpsecPolicy-PolicyName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfIpsecPolicy_PolicyName.setStatus('mandatory')
mibProfIpsecPolicy_FilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 2), DisplayString()).setLabel("mibProfIpsecPolicy-FilterName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_FilterName.setStatus('mandatory')
mibProfIpsecPolicy_KeyManagement = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("ike", 2)))).setLabel("mibProfIpsecPolicy-KeyManagement").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_KeyManagement.setStatus('mandatory')
mibProfIpsecPolicy_IpsecProposals = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 4), DisplayString()).setLabel("mibProfIpsecPolicy-IpsecProposals").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_IpsecProposals.setStatus('mandatory')
mibProfIpsecPolicy_PrimaryTunnelAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 5), IpAddress()).setLabel("mibProfIpsecPolicy-PrimaryTunnelAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_PrimaryTunnelAddress.setStatus('mandatory')
mibProfIpsecPolicy_SecondaryTunnelAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 6), IpAddress()).setLabel("mibProfIpsecPolicy-SecondaryTunnelAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_SecondaryTunnelAddress.setStatus('mandatory')
mibProfIpsecPolicy_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfIpsecPolicy-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBIPSECPOLICY-MIB", mibmibProfIpsecPolicy=mibmibProfIpsecPolicy, mibProfIpsecPolicy_IpsecProposals=mibProfIpsecPolicy_IpsecProposals, mibProfIpsecPolicy_PolicyName=mibProfIpsecPolicy_PolicyName, mibmibProfIpsecPolicyEntry=mibmibProfIpsecPolicyEntry, mibProfIpsecPolicy_KeyManagement=mibProfIpsecPolicy_KeyManagement, mibmibProfIpsecPolicyTable=mibmibProfIpsecPolicyTable, DisplayString=DisplayString, mibProfIpsecPolicy_PrimaryTunnelAddress=mibProfIpsecPolicy_PrimaryTunnelAddress, mibProfIpsecPolicy_SecondaryTunnelAddress=mibProfIpsecPolicy_SecondaryTunnelAddress, mibProfIpsecPolicy_FilterName=mibProfIpsecPolicy_FilterName, mibProfIpsecPolicy_Action_o=mibProfIpsecPolicy_Action_o)
