#
# PySNMP MIB module ASCEND-MIBIPSECPOLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPSECPOLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter32, iso, ModuleIdentity, MibIdentifier, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, NotificationType, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "iso", "ModuleIdentity", "MibIdentifier", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "NotificationType", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibmibProfIpsecPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 167))
mibmibProfIpsecPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 167, 1), )
if mibBuilder.loadTexts: mibmibProfIpsecPolicyTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfIpsecPolicyTable.setDescription('A list of mibmibProfIpsecPolicy profile entries.')
mibmibProfIpsecPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPSECPOLICY-MIB", "mibProfIpsecPolicy-PolicyName"))
if mibBuilder.loadTexts: mibmibProfIpsecPolicyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfIpsecPolicyEntry.setDescription('A mibmibProfIpsecPolicy entry containing objects that maps to the parameters of mibmibProfIpsecPolicy profile.')
mibProfIpsecPolicy_PolicyName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 1), DisplayString()).setLabel("mibProfIpsecPolicy-PolicyName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfIpsecPolicy_PolicyName.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_PolicyName.setDescription('The name of this IPSEC Policy.')
mibProfIpsecPolicy_FilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 2), DisplayString()).setLabel("mibProfIpsecPolicy-FilterName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_FilterName.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_FilterName.setDescription('The name of the Filter containing the IPSec selectors for this Policy. Current IPSec policy will be applied only to the traffic that the filter forwards. Traffic not forwarded by the filter will not necessarily be dropped, it may have a chance to match another policy.')
mibProfIpsecPolicy_KeyManagement = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("ike", 2)))).setLabel("mibProfIpsecPolicy-KeyManagement").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_KeyManagement.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_KeyManagement.setDescription('This determines whether static key or dynamic key (IKE) is used for this policy.')
mibProfIpsecPolicy_IpsecProposals = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 4), DisplayString()).setLabel("mibProfIpsecPolicy-IpsecProposals").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_IpsecProposals.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_IpsecProposals.setDescription('The name of the IPSEC Protection Suite profile to be used for IPSec SAs negotiation for the traffic encompassed by this policy. This may be a unique proposal or the first element of a list of proposals.')
mibProfIpsecPolicy_PrimaryTunnelAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 5), IpAddress()).setLabel("mibProfIpsecPolicy-PrimaryTunnelAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_PrimaryTunnelAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_PrimaryTunnelAddress.setDescription('IP address of the primary IPSEC peer (tunnel mode only).')
mibProfIpsecPolicy_SecondaryTunnelAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 6), IpAddress()).setLabel("mibProfIpsecPolicy-SecondaryTunnelAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_SecondaryTunnelAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_SecondaryTunnelAddress.setDescription('IP address of the secondary IPSEC peer (tunnel mode only).')
mibProfIpsecPolicy_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 167, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfIpsecPolicy-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfIpsecPolicy_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfIpsecPolicy_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBIPSECPOLICY-MIB", mibmibProfIpsecPolicy=mibmibProfIpsecPolicy, mibProfIpsecPolicy_IpsecProposals=mibProfIpsecPolicy_IpsecProposals, DisplayString=DisplayString, mibProfIpsecPolicy_KeyManagement=mibProfIpsecPolicy_KeyManagement, mibProfIpsecPolicy_SecondaryTunnelAddress=mibProfIpsecPolicy_SecondaryTunnelAddress, mibmibProfIpsecPolicyEntry=mibmibProfIpsecPolicyEntry, mibProfIpsecPolicy_Action_o=mibProfIpsecPolicy_Action_o, mibProfIpsecPolicy_FilterName=mibProfIpsecPolicy_FilterName, mibmibProfIpsecPolicyTable=mibmibProfIpsecPolicyTable, mibProfIpsecPolicy_PrimaryTunnelAddress=mibProfIpsecPolicy_PrimaryTunnelAddress, mibProfIpsecPolicy_PolicyName=mibProfIpsecPolicy_PolicyName)