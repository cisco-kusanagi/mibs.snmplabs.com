#
# PySNMP MIB module HUAWEI-TFTPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TFTPC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, NotificationType, Counter32, IpAddress, Bits, Unsigned32, ModuleIdentity, MibIdentifier, TimeTicks, iso, ObjectIdentity, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Counter32", "IpAddress", "Bits", "Unsigned32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwTftpc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197))
hwTftpc.setRevisions(('2010-06-01 00:00', '2010-12-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwTftpc.setRevisionsDescriptions(('The initial revision of this MIB module.', 'Modified by z47250 for fixing SimpleTester compile errors.',))
if mibBuilder.loadTexts: hwTftpc.setLastUpdated('201012080000Z')
if mibBuilder.loadTexts: hwTftpc.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwTftpc.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwTftpc.setDescription('The HUAWEI-TFTPC-MIB which contains objects manages the TFTP client configuration. ')
hwTftpClientInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2))
hwTftpClientSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTftpClientSourceAddress.setStatus('current')
if mibBuilder.loadTexts: hwTftpClientSourceAddress.setDescription('Tftp client IP address. ')
hwTftpClientSourceInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTftpClientSourceInterfaceName.setStatus('current')
if mibBuilder.loadTexts: hwTftpClientSourceInterfaceName.setDescription('Tftp client source interface name. ')
mibBuilder.exportSymbols("HUAWEI-TFTPC-MIB", hwTftpClientInfo=hwTftpClientInfo, PYSNMP_MODULE_ID=hwTftpc, hwTftpc=hwTftpc, hwTftpClientSourceAddress=hwTftpClientSourceAddress, hwTftpClientSourceInterfaceName=hwTftpClientSourceInterfaceName)
