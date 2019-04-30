#
# PySNMP MIB module HUAWEI-TFTPC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TFTPC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter64, Gauge32, Unsigned32, IpAddress, iso, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hwTftpc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197))
hwTftpc.setRevisions(('2010-06-01 00:00', '2010-12-08 00:00',))
if mibBuilder.loadTexts: hwTftpc.setLastUpdated('201012080000Z')
if mibBuilder.loadTexts: hwTftpc.setOrganization('Huawei Technologies co.,Ltd.')
hwTftpClientInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2))
hwTftpClientSourceAddress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTftpClientSourceAddress.setStatus('current')
hwTftpClientSourceInterfaceName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTftpClientSourceInterfaceName.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-TFTPC-MIB", hwTftpClientInfo=hwTftpClientInfo, hwTftpc=hwTftpc, hwTftpClientSourceInterfaceName=hwTftpClientSourceInterfaceName, hwTftpClientSourceAddress=hwTftpClientSourceAddress, PYSNMP_MODULE_ID=hwTftpc)
