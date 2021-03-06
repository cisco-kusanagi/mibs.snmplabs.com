#
# PySNMP MIB module ZHONE-IUA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-IUA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Integer32, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Bits, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Bits", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zhoneIua, = mibBuilder.importSymbols("Zhone", "zhoneIua")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhoneIuaModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1))
zhoneIuaModule.setRevisions(('2009-05-25 23:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhoneIuaModule.setRevisionsDescriptions(('V01.00.00 - Initial revision',))
if mibBuilder.loadTexts: zhoneIuaModule.setLastUpdated('200905270656Z')
if mibBuilder.loadTexts: zhoneIuaModule.setOrganization('Zhone Technologies.')
if mibBuilder.loadTexts: zhoneIuaModule.setContactInfo(' Postal: Zhone Technologies, Inc. @ Zhone Way 7001 Oakport Street Oakland, CA 94621 USA Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: zhoneIuaModule.setDescription('IUA server configuration for Zhone products')
zhoneIuaServerCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1))
zhoneIuaServerTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1), )
if mibBuilder.loadTexts: zhoneIuaServerTable.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerTable.setDescription('Table of IUA Server addresses.')
zhoneIuaServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "ZHONE-IUA-MIB", "zhoneIuaServerAddressIndex"))
if mibBuilder.loadTexts: zhoneIuaServerEntry.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerEntry.setDescription('An entry within the table. Indexed by applIndex, which is an index to voip-server-entry, and a user specified unique number.')
zhoneIuaServerAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: zhoneIuaServerAddressIndex.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerAddressIndex.setDescription("A unique identifier of a server address. When multiple addresses are configured and if one address isn't reachable, then another can be tried. ")
zhoneIuaServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 2), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerRowStatus.setDescription('Row Status is used to create, modify or delete an entry.')
zhoneIuaServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerAddress.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerAddress.setDescription('This object specifies the address of IUA server.')
zhoneIuaServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 15, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(9900)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zhoneIuaServerPortNumber.setStatus('current')
if mibBuilder.loadTexts: zhoneIuaServerPortNumber.setDescription('Specifies the port number fro IUA server')
mibBuilder.exportSymbols("ZHONE-IUA-MIB", zhoneIuaServerCfg=zhoneIuaServerCfg, zhoneIuaServerAddressIndex=zhoneIuaServerAddressIndex, zhoneIuaServerTable=zhoneIuaServerTable, zhoneIuaServerPortNumber=zhoneIuaServerPortNumber, zhoneIuaServerAddress=zhoneIuaServerAddress, PYSNMP_MODULE_ID=zhoneIuaModule, zhoneIuaServerEntry=zhoneIuaServerEntry, zhoneIuaServerRowStatus=zhoneIuaServerRowStatus, zhoneIuaModule=zhoneIuaModule)
